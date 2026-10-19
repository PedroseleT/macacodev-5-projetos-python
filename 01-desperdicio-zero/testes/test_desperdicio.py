import json
import sys
import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solucao"))

from desperdicio.arquivos import gravar_json, ler_json
from desperdicio.dominio import (
    cadastrar,
    data_de_entrada,
    novo_estado,
    quantidade_valida,
    remover,
    situacao,
    validar_estado,
)
from desperdicio.terminal import executar


class TestAlimentos(unittest.TestCase):
    def test_cadastrar_sem_alterar_original(self):
        original = novo_estado()
        novo = cadastrar(original, " Banana ", "1,5", "20/10/2026")
        self.assertEqual(original["alimentos"], [])
        self.assertEqual(novo["alimentos"][0]["quantidade"], 1.5)
        self.assertEqual(novo["alimentos"][0]["nome"], "Banana")
        validar_estado(novo)

    def test_quantidades_invalidas(self):
        for valor in [0, -1, "banana", "NaN", "inf", True, None, 1e20]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                quantidade_valida(valor)

    def test_datas_invalidas(self):
        for valor in ["31/02/2026", "1/2/2026", "2026-01-01", "", None]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                data_de_entrada(valor)

    def test_ano_bissexto(self):
        self.assertEqual(data_de_entrada("29/02/2028"), "2028-02-29")

    def test_vencido_proximo_e_em_dia(self):
        hoje = date(2026, 10, 18)
        for validade, esperado in [
            ("2026-10-17", "vencido"),
            ("2026-10-18", "proximo"),
            ("2026-10-21", "proximo"),
            ("2026-10-22", "em_dia"),
        ]:
            self.assertEqual(situacao({"validade": validade}, hoje), esperado)

    def test_remover_e_nao_reutilizar_id(self):
        estado = cadastrar(novo_estado(), "Banana", 2, "20/10/2026")
        estado = remover(estado, 1)
        estado = cadastrar(estado, "Arroz", 1, "21/10/2026")
        self.assertEqual(estado["alimentos"][0]["id"], 2)
        with self.assertRaises(ValueError):
            remover(estado, 99)

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            cadastrar(novo_estado(), "  ", 1, "20/10/2026")

    def test_persistencia_e_arquivo_ausente(self):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "nova" / "alimentos.json"
            self.assertEqual(ler_json(caminho, novo_estado()), novo_estado())
            estado = cadastrar(novo_estado(), "Maçã", 3, "20/10/2026")
            gravar_json(caminho, estado)
            self.assertEqual(ler_json(caminho, novo_estado()), estado)

    def test_json_corrompido_nao_e_apagado(self):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            caminho.write_text("{quebrou", encoding="utf-8")
            with self.assertRaises(ValueError):
                ler_json(caminho, novo_estado())
            self.assertEqual(caminho.read_text(encoding="utf-8"), "{quebrou")

    def test_estrutura_corrompida(self):
        for estado in [
            [],
            {"versao": 2},
            {"versao": 1, "proximo_id": True, "alimentos": []},
        ]:
            with self.assertRaises(ValueError):
                validar_estado(estado)

    def test_falha_de_gravacao_preserva_destino(self):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            gravar_json(caminho, {"anterior": 1})
            with patch("pathlib.Path.replace", side_effect=OSError("sem acesso")):
                with self.assertRaises(OSError):
                    gravar_json(caminho, {"novo": 2})
            self.assertEqual(json.loads(caminho.read_text()), {"anterior": 1})
            self.assertEqual(list(Path(pasta).glob("*.tmp")), [])

    def test_menu_cadastro_reinicio_remocao(self):
        with TemporaryDirectory() as pasta, patch("builtins.print"):
            caminho = Path(pasta) / "dados.json"
            with patch(
                "builtins.input",
                side_effect=[
                    "x",
                    "1",
                    "Banana",
                    "2",
                    "20/10/2026",
                    "2",
                    "3",
                    "4",
                    "0",
                ],
            ):
                self.assertEqual(executar(caminho), 0)
            self.assertEqual(len(ler_json(caminho, {})["alimentos"]), 1)
            with patch("builtins.input", side_effect=["5", "1", "0"]):
                self.assertEqual(executar(caminho), 0)
            self.assertEqual(ler_json(caminho, {})["alimentos"], [])


if __name__ == "__main__":
    unittest.main()
