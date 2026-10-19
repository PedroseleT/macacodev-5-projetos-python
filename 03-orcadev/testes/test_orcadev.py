import sys
import unittest
from datetime import date
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solucao"))

from orcadev.arquivos import gravar_json, ler_json
from orcadev.dominio import (
    cadastrar_cliente,
    calcular_totais,
    criar_item,
    criar_orcamento,
    dinheiro,
    formatar_orcamento,
    novo_estado,
    validar_estado,
)
from orcadev.terminal import executar


class TestOrcamentos(unittest.TestCase):
    def estado_com_cliente(self):
        return cadastrar_cliente(novo_estado(), "Cliente de demonstração")

    def test_decimal_sem_erro_binario(self):
        totais = calcular_totais([criar_item("Revisão", 3, "0,10")])
        self.assertEqual(totais["total"], Decimal("0.30"))
        self.assertIsInstance(totais["total"], Decimal)

    def test_multiplos_servicos_e_desconto(self):
        itens = [criar_item("Página", 2, "10.50"), criar_item("Revisão", 1, "9")]
        self.assertEqual(
            calcular_totais(itens, "5"),
            {
                "subtotal": Decimal("30.00"),
                "desconto": Decimal("5.00"),
                "total": Decimal("25.00"),
            },
        )

    def test_desconto_total_permitido(self):
        self.assertEqual(
            calcular_totais([criar_item("Teste", 1, "10")], "10")["total"], 0
        )

    def test_descontos_invalidos(self):
        for valor in ["-1", "11", "NaN"]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                calcular_totais([criar_item("Teste", 1, "10")], valor)

    def test_dinheiro_invalido(self):
        for valor in [0.1, True, "NaN", "Infinity", "1.001", "-1", None, "1e100"]:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                dinheiro(valor)

    def test_servico_invalido(self):
        for descricao, quantidade, preco in [
            ("", 1, "2"),
            ("A", 0, "2"),
            ("A", "1.5", "2"),
            ("A", 1, "0"),
        ]:
            with self.subTest(quantidade=quantidade), self.assertRaises(ValueError):
                criar_item(descricao, quantidade, preco)

    def test_sem_servicos(self):
        with self.assertRaises(ValueError):
            calcular_totais([])

    def test_cliente_inexistente(self):
        with self.assertRaises(ValueError):
            criar_orcamento(novo_estado(), 99, [criar_item("A", 1, "1")])

    def test_multiplos_orcamentos_imutaveis(self):
        inicial = self.estado_com_cliente()
        novo = criar_orcamento(inicial, 1, [criar_item("A", 1, "1")])
        novo = criar_orcamento(novo, 1, [criar_item("B", 2, "2")])
        self.assertEqual(inicial["orcamentos"], [])
        self.assertEqual([o["id"] for o in novo["orcamentos"]], [1, 2])
        validar_estado(novo)

    def test_texto_e_persistencia(self):
        estado = criar_orcamento(
            self.estado_com_cliente(),
            1,
            [criar_item("Revisão", 2, "12.50")],
            "5",
            date(2026, 10, 18),
        )
        texto = formatar_orcamento(estado, 1)
        self.assertIn("TOTAL: R$ 20,00", texto)
        self.assertIn("2026-10-18", texto)
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            gravar_json(caminho, estado)
            carregado = ler_json(caminho, {})
            validar_estado(carregado)
            self.assertEqual(formatar_orcamento(carregado, 1), texto)

    def test_orcamento_orfao_rejeitado(self):
        estado = criar_orcamento(
            self.estado_com_cliente(), 1, [criar_item("A", 1, "1")]
        )
        estado["clientes"] = []
        with self.assertRaises(ValueError):
            validar_estado(estado)

    def test_menu_completo_exporta_texto(self):
        with TemporaryDirectory() as pasta, patch("builtins.print"):
            caminho = Path(pasta) / "dados.json"
            entradas = [
                "1",
                "Cliente demonstração",
                "2",
                "1",
                "1",
                "Revisão",
                "2",
                "12,50",
                "5",
                "3",
                "4",
                "1",
                "0",
            ]
            with patch("builtins.input", side_effect=entradas):
                self.assertEqual(executar(caminho), 0)
            self.assertIn(
                "TOTAL: R$ 20,00",
                (Path(pasta) / "orcamentos/orcamento-0001.txt").read_text(
                    encoding="utf-8"
                ),
            )


if __name__ == "__main__":
    unittest.main()
