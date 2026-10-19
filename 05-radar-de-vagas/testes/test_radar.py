import csv
import sys
import unittest
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "solucao"))

from radar.arquivos import gravar_json, ler_json
from radar.dominio import (
    STATUS,
    atualizar,
    cadastrar,
    estatisticas,
    excluir,
    filtrar,
    novo_estado,
    pesquisar,
    validar_estado,
)
from radar.exportacao import exportar_csv, gerar_csv
from radar.terminal import executar


class TestRadar(unittest.TestCase):
    def adicionar(
        self,
        estado=None,
        empresa="Empresa de demonstração",
        status="Interesse",
        data="",
    ):
        return cadastrar(
            estado or novo_estado(),
            empresa,
            "Estágio Python",
            "https://example.org/vaga",
            data,
            status,
        )

    def test_cadastro_interesse_sem_data(self):
        estado = self.adicionar()
        self.assertIsNone(estado["candidaturas"][0]["data_candidatura"])
        validar_estado(estado)

    def test_enviada_exige_data(self):
        with self.assertRaises(ValueError):
            self.adicionar(status="Candidatura enviada")
        estado = self.adicionar(status="Candidatura enviada", data="18/10/2026")
        self.assertEqual(estado["candidaturas"][0]["data_candidatura"], "2026-10-18")

    def test_todos_status_validos(self):
        for status in STATUS:
            estado = self.adicionar(status=status, data="18/10/2026")
            self.assertEqual(estado["candidaturas"][0]["status"], status)

    def test_campos_e_links_invalidos(self):
        casos = [
            "javascript:alert(1)",
            "ftp://example.org",
            "https://u:senha@example.org",
            "sem-link",
            "https://example.org/tem espaço",
            "http://example.org:99999",
        ]
        for link in casos:
            with self.subTest(link=link), self.assertRaises(ValueError):
                cadastrar(novo_estado(), "Empresa", "Cargo", link, "", "Interesse")

    def test_textos_vazios_e_status_invalido(self):
        for empresa, status in [(" ", "Interesse"), ("Empresa", "Contratado talvez")]:
            with self.assertRaises(ValueError):
                self.adicionar(empresa=empresa, status=status)

    def test_data_invalida(self):
        with self.assertRaises(ValueError):
            self.adicionar(data="31/02/2026")

    def test_atualizar_sem_mudar_original(self):
        estado = self.adicionar()
        novo = atualizar(
            estado,
            1,
            {
                "cargo": "Dev Python",
                "status": "Entrevista",
                "data_candidatura": "18/10/2026",
            },
        )
        self.assertEqual(novo["candidaturas"][0]["cargo"], "Dev Python")
        self.assertEqual(estado["candidaturas"][0]["status"], "Interesse")
        self.assertEqual(
            novo["candidaturas"][0]["criada_em"], estado["candidaturas"][0]["criada_em"]
        )

    def test_atualizacao_invalida_atomica(self):
        estado = self.adicionar()
        with self.assertRaises(ValueError):
            atualizar(estado, 1, {"cargo": "Novo cargo", "status": "Entrevista"})
        self.assertEqual(estado["candidaturas"][0]["cargo"], "Estágio Python")
        with self.assertRaises(ValueError):
            atualizar(estado, 1, {"id": 99})

    def test_excluir_e_id_inexistente(self):
        estado = excluir(self.adicionar(), 1)
        self.assertEqual(estado["candidaturas"], [])
        self.assertEqual(self.adicionar(estado)["candidaturas"][0]["id"], 2)
        with self.assertRaises(ValueError):
            excluir(estado, 99)
        with self.assertRaises(ValueError):
            atualizar(estado, 99, {"cargo": "Novo"})

    def test_pesquisa_parcial_sem_distinguir_caixa(self):
        estado = self.adicionar(empresa="Banana Sistemas")
        estado = self.adicionar(estado, empresa="Outra empresa")
        self.assertEqual(len(pesquisar(estado, "BANANA")), 1)
        self.assertEqual(pesquisar(estado, "inexistente"), [])

    def test_filtro_e_estatisticas(self):
        estado = self.adicionar()
        estado = self.adicionar(estado, status="Entrevista", data="18/10/2026")
        self.assertEqual(len(filtrar(estado, "entrevista")), 1)
        self.assertEqual(estatisticas(estado)["total"], 2)
        self.assertEqual(estatisticas(estado)["por_status"]["Entrevista"], 1)

    def test_csv_acentos_virgulas_e_formula(self):
        estado = self.adicionar(empresa='Empresa, "Demonstração"')
        estado = self.adicionar(estado, empresa="=1+1")
        linhas = list(csv.DictReader(StringIO(gerar_csv(estado))))
        self.assertEqual(linhas[0]["empresa"], 'Empresa, "Demonstração"')
        self.assertEqual(linhas[1]["empresa"], "'=1+1")
        self.assertEqual(estado["candidaturas"][1]["empresa"], "=1+1")

    def test_persistencia_e_csv_em_arquivo(self):
        estado = self.adicionar()
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            gravar_json(caminho, estado)
            recuperado = ler_json(caminho, {})
            validar_estado(recuperado)
            self.assertEqual(recuperado, estado)
            destino = Path(pasta) / "exportacoes" / "dados.csv"
            exportar_csv(recuperado, destino)
            self.assertEqual(
                len(
                    list(csv.DictReader(StringIO(destino.read_text(encoding="utf-8"))))
                ),
                1,
            )

    def test_estado_vazio_e_csv_so_cabecalho(self):
        self.assertEqual(estatisticas(novo_estado())["total"], 0)
        self.assertEqual(list(csv.DictReader(StringIO(gerar_csv(novo_estado())))), [])

    def test_id_duplicado_rejeitado(self):
        estado = self.adicionar()
        estado["candidaturas"].append(dict(estado["candidaturas"][0]))
        with self.assertRaises(ValueError):
            validar_estado(estado)

    def test_menu_crud_e_exportacao(self):
        with TemporaryDirectory() as pasta, patch("builtins.print"):
            caminho = Path(pasta) / "dados.json"
            entradas = [
                "1",
                "Empresa demonstração",
                "Estágio",
                "https://example.org/vaga",
                "1",
                "",
                "2",
                "3",
                "1",
                "4",
                "demonstração",
                "5",
                "1",
                "status",
                "3",
                "18/10/2026",
                "7",
                "8",
                "6",
                "1",
                "SIM",
                "0",
            ]
            with patch("builtins.input", side_effect=entradas):
                self.assertEqual(executar(caminho), 0)
            self.assertEqual(ler_json(caminho, {})["candidaturas"], [])
            self.assertTrue((Path(pasta) / "exportacoes/candidaturas.csv").exists())


if __name__ == "__main__":
    unittest.main()
