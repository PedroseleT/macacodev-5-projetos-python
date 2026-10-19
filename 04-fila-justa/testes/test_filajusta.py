import sys
import unittest
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solucao"))

from filajusta.arquivos import gravar_json, ler_json
from filajusta.dominio import (
    chamar_proxima,
    concluir,
    estatisticas,
    gerar_senha,
    novo_estado,
    rotulo,
    validar_estado,
)
from filajusta.terminal import executar


class TestFila(unittest.TestCase):
    def preparar(self):
        estado = novo_estado()
        for tipo in ["comum", "prioritaria", "prioritaria", "comum", "prioritaria"]:
            estado = gerar_senha(estado, tipo)
        return estado

    def test_intercalacao_e_fifo(self):
        estado = self.preparar()
        chamadas = []
        for _ in range(5):
            estado = chamar_proxima(estado)
            chamadas.append(rotulo(estado["em_atendimento"]))
            estado = concluir(estado)
        self.assertEqual(chamadas, ["P0002", "P0003", "C0001", "P0005", "C0004"])
        self.assertEqual(estatisticas(estado)["concluidos"], 5)
        validar_estado(estado)

    def test_fila_vazia(self):
        with self.assertRaisesRegex(ValueError, "vazia"):
            chamar_proxima(novo_estado())

    def test_concluir_sem_chamada(self):
        with self.assertRaises(ValueError):
            concluir(novo_estado())

    def test_nao_chamar_durante_atendimento(self):
        estado = chamar_proxima(self.preparar())
        with self.assertRaises(ValueError):
            chamar_proxima(estado)

    def test_categoria_invalida(self):
        with self.assertRaises(ValueError):
            gerar_senha(novo_estado(), "vip")

    def test_somente_prioritaria_nao_bloqueia(self):
        estado = novo_estado()
        for _ in range(4):
            estado = gerar_senha(estado, "prioritaria")
        for _ in range(4):
            estado = concluir(chamar_proxima(estado))
        self.assertEqual(estatisticas(estado)["prioritarios_concluidos"], 4)

    def test_comum_chega_apos_duas_prioritarias(self):
        estado = novo_estado()
        for _ in range(3):
            estado = gerar_senha(estado, "prioritaria")
        estado = concluir(chamar_proxima(estado))
        estado = concluir(chamar_proxima(estado))
        estado = gerar_senha(estado, "comum")
        estado = chamar_proxima(estado)
        self.assertEqual(estado["em_atendimento"]["tipo"], "comum")

    def test_estado_original_preservado(self):
        estado = self.preparar()
        copia = deepcopy(estado)
        chamar_proxima(estado)
        self.assertEqual(estado, copia)

    def test_recuperacao_preserva_turno_e_atendimento(self):
        estado = chamar_proxima(self.preparar())
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "fila.json"
            gravar_json(caminho, estado)
            novo = ler_json(caminho, {})
            validar_estado(novo)
            self.assertEqual(novo, estado)
            novo = chamar_proxima(concluir(novo))
            self.assertEqual(rotulo(novo["em_atendimento"]), "P0003")

    def test_senha_duplicada_rejeitada(self):
        estado = self.preparar()
        estado["comum"].append(deepcopy(estado["comum"][0]))
        with self.assertRaises(ValueError):
            validar_estado(estado)

    def test_ordem_trocada_rejeitada(self):
        estado = self.preparar()
        estado["comum"].reverse()
        with self.assertRaises(ValueError):
            validar_estado(estado)

    def test_contagem_e_historico(self):
        estado = concluir(chamar_proxima(self.preparar()))
        self.assertEqual(
            estatisticas(estado),
            {
                "concluidos": 1,
                "comuns_concluidos": 0,
                "prioritarios_concluidos": 1,
                "aguardando": 4,
                "em_atendimento": 0,
            },
        )
        self.assertIn("concluida_em", estado["historico"][0])

    def test_menu_gerar_chamar_concluir(self):
        with TemporaryDirectory() as pasta, patch("builtins.print"):
            caminho = Path(pasta) / "fila.json"
            with patch(
                "builtins.input",
                side_effect=["4", "1", "2", "3", "4", "5", "6", "7", "0"],
            ):
                self.assertEqual(executar(caminho), 0)
            estado = ler_json(caminho, {})
            self.assertEqual(len(estado["historico"]), 1)
            self.assertEqual(estado["historico"][0]["tipo"], "prioritaria")


if __name__ == "__main__":
    unittest.main()
