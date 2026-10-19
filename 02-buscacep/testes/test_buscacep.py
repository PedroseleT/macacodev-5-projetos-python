import json
import sys
import unittest
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solucao"))

from buscacep.arquivos import gravar_json, ler_json
from buscacep.dominio import novo_estado, registrar, validar_estado
from buscacep.servico import (
    CepNaoEncontrado,
    consultar,
    interpretar_resposta,
    normalizar_cep,
)
from buscacep.terminal import executar

ENDERECO = {
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
}


def abrir_falso(conteudo, status=200):
    resposta = MagicMock()
    resposta.__enter__.return_value = resposta
    resposta.status = status
    resposta.read.return_value = conteudo
    return MagicMock(return_value=resposta)


class TestBuscaCep(unittest.TestCase):
    def test_formatos_validos(self):
        for cep in ["01001-000", "01001000", " 01001000 "]:
            self.assertEqual(normalizar_cep(cep), "01001000")

    def test_formatos_invalidos(self):
        for cep in ["123", "01001 000", "abcdefgh", "１２３４５６７８", None]:
            with self.subTest(cep=cep), self.assertRaises(ValueError):
                normalizar_cep(cep)

    def test_consulta_valida_com_timeout(self):
        abrir = abrir_falso(json.dumps(ENDERECO).encode())
        self.assertEqual(consultar("01001000", abrir), ENDERECO)
        abrir.assert_called_once_with(
            "https://viacep.com.br/ws/01001000/json/", timeout=10
        )

    def test_invalido_nao_faz_http(self):
        abrir = MagicMock()
        with self.assertRaises(ValueError):
            consultar("errado", abrir)
        abrir.assert_not_called()

    def test_cep_nao_encontrado(self):
        for valor in [True, "true"]:
            abrir = abrir_falso(json.dumps({"erro": valor}).encode())
            with self.assertRaises(CepNaoEncontrado):
                consultar("99999999", abrir)

    def test_falha_de_conexao_e_timeout(self):
        for erro in [URLError("offline"), TimeoutError("demorou")]:
            with self.subTest(erro=erro), self.assertRaisesRegex(ValueError, "conexão"):
                consultar("01001000", MagicMock(side_effect=erro))

    def test_erro_http(self):
        erro = HTTPError("url", 503, "fora", {}, BytesIO())
        with self.assertRaisesRegex(ValueError, "503"):
            consultar("01001000", MagicMock(side_effect=erro))

    def test_resposta_json_invalida(self):
        for conteudo in [b"<html>erro</html>", b"\xff", b"[]", b"null", b"{}"]:
            with self.subTest(conteudo=conteudo), self.assertRaises(ValueError):
                consultar("01001000", abrir_falso(conteudo))

    def test_status_inesperado(self):
        with self.assertRaisesRegex(ValueError, "status"):
            consultar("01001000", abrir_falso(b"{}", status=204))

    def test_cep_da_resposta_diferente(self):
        dados = dict(ENDERECO, cep="20000-000")
        with self.assertRaisesRegex(ValueError, "corresponde"):
            consultar("01001000", abrir_falso(json.dumps(dados).encode()))

    def test_cep_generico_sem_rua_e_valido(self):
        dados = dict(ENDERECO, logradouro="", bairro="")
        self.assertEqual(interpretar_resposta(dados)["logradouro"], "")

    def test_limite_da_resposta(self):
        with self.assertRaisesRegex(ValueError, "limite"):
            consultar("01001000", abrir_falso(b" " * 1_000_001))

    def test_registro_persistencia_e_repeticao(self):
        estado = novo_estado()
        novo = registrar(estado, ENDERECO, "2026-10-18T10:00:00+00:00")
        self.assertEqual(estado["consultas"], [])
        novo = registrar(novo, ENDERECO)
        validar_estado(novo)
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "historico.json"
            gravar_json(caminho, novo)
            self.assertEqual(ler_json(caminho, {}), novo)

    def test_historico_invalido(self):
        with self.assertRaises(ValueError):
            validar_estado({"versao": 1, "consultas": [{"endereco": ENDERECO}]})

    def test_menu_repete_apos_falha_e_so_salva_valido(self):
        with TemporaryDirectory() as pasta, patch("builtins.print"):
            caminho = Path(pasta) / "historico.json"
            with patch(
                "builtins.input", side_effect=["1", "123", "1", "01001000", "2", "0"]
            ):
                with patch(
                    "buscacep.terminal.consultar",
                    side_effect=[ValueError("CEP inválido"), ENDERECO],
                ):
                    self.assertEqual(executar(caminho), 0)
            self.assertEqual(len(ler_json(caminho, {})["consultas"]), 1)


if __name__ == "__main__":
    unittest.main()
