"""Integração por subprocessos: os programas não dependem do diretório atual."""

import ast
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

RAIZ = Path(__file__).resolve().parents[1]
PROJETOS = sorted(p for p in RAIZ.glob("[0-9][0-9]-*") if p.is_dir())


def executar(arquivo, pasta, entrada, dados=None):
    comando = [sys.executable, str(arquivo)]
    if dados is not None:
        comando.extend(["--dados", str(dados)])
    return subprocess.run(
        comando,
        input=entrada,
        text=True,
        encoding="utf-8",
        capture_output=True,
        timeout=15,
        cwd=pasta,
        env=dict(os.environ, PYTHONUTF8="1"),
    )


class TestTrilha(unittest.TestCase):
    def test_cinco_projetos_com_documentacao_completa(self):
        self.assertEqual(len(PROJETOS), 5)
        for projeto in PROJETOS:
            with self.subTest(projeto=projeto.name):
                for nome in ["README.md", "dicas.md", "desafios.md", "checklist.md"]:
                    self.assertGreater(
                        len((projeto / nome).read_text(encoding="utf-8")), 100
                    )
                tutoriais = sorted((projeto / "passo-a-passo").glob("*.md"))
                self.assertEqual(len(tutoriais), 5)
                for tutorial in tutoriais:
                    self.assertGreater(
                        len(tutorial.read_text(encoding="utf-8").split()), 150
                    )

    def test_sintaxe_compativel_com_python_311(self):
        for arquivo in RAIZ.rglob("*.py"):
            if ".venv" not in arquivo.parts:
                with self.subTest(arquivo=str(arquivo.relative_to(RAIZ))):
                    ast.parse(
                        arquivo.read_text(encoding="utf-8"), feature_version=(3, 11)
                    )

    def test_primeira_execucao_fora_da_raiz(self):
        with TemporaryDirectory(prefix="macacodev espaço ") as pasta:
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    dados = Path(pasta) / projeto.name / "dados com espaço.json"
                    processo = executar(
                        projeto / "solucao/main.py", pasta, "x\n0\n", dados
                    )
                    self.assertEqual(processo.returncode, 0, processo.stderr)
                    self.assertIn("inválida", processo.stdout)
                    self.assertFalse(dados.exists())

    def test_codigos_iniciais_executam_sem_solucao(self):
        with TemporaryDirectory() as pasta:
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    processo = executar(
                        projeto / "codigo-inicial/main.py", pasta, "1\n0\n"
                    )
                    self.assertEqual(processo.returncode, 0, processo.stderr)
                    self.assertNotIn("Traceback", processo.stderr)
                    fontes = "\n".join(
                        p.read_text(encoding="utf-8")
                        for p in (projeto / "codigo-inicial").glob("*.py")
                    )
                    self.assertNotIn("from solucao", fontes)

    def test_eof_nao_deixa_menu_preso(self):
        with TemporaryDirectory() as pasta:
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    processo = executar(
                        projeto / "solucao/main.py",
                        pasta,
                        "",
                        Path(pasta) / "dados.json",
                    )
                    self.assertEqual(processo.returncode, 0, processo.stderr)

    def test_arquivo_corrompido_preservado_em_todos(self):
        with TemporaryDirectory() as pasta:
            dados = Path(pasta) / "corrompido.json"
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    dados.write_text("{incompleto", encoding="utf-8")
                    processo = executar(
                        projeto / "solucao/main.py", pasta, "0\n", dados
                    )
                    self.assertEqual(processo.returncode, 1)
                    self.assertEqual(dados.read_text(encoding="utf-8"), "{incompleto")

    def test_json_valido_mas_estrutura_errada_preservada(self):
        with TemporaryDirectory() as pasta:
            dados = Path(pasta) / "errado.json"
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    dados.write_text(json.dumps({"versao": 999}), encoding="utf-8")
                    processo = executar(
                        projeto / "solucao/main.py", pasta, "0\n", dados
                    )
                    self.assertEqual(processo.returncode, 1)
                    self.assertEqual(json.loads(dados.read_text()), {"versao": 999})

    def test_booleano_nao_e_versao_inteira(self):
        import importlib

        pacotes = ["desperdicio", "buscacep", "orcadev", "filajusta", "radar"]
        for projeto, pacote in zip(PROJETOS, pacotes):
            with self.subTest(projeto=projeto.name):
                sys.path.insert(0, str(projeto / "solucao"))
                modulo = importlib.import_module(f"{pacote}.dominio")
                estado = modulo.novo_estado()
                estado["versao"] = True
                with self.assertRaises(ValueError):
                    modulo.validar_estado(estado)

    def test_gravacao_interrompida_preserva_arquivo_em_cada_projeto(self):
        import importlib
        from unittest.mock import patch

        pacotes = ["desperdicio", "buscacep", "orcadev", "filajusta", "radar"]
        with TemporaryDirectory() as pasta:
            for projeto, pacote in zip(PROJETOS, pacotes):
                with self.subTest(projeto=projeto.name):
                    sys.path.insert(0, str(projeto / "solucao"))
                    arquivos = importlib.import_module(f"{pacote}.arquivos")
                    caminho = Path(pasta) / "dados.json"
                    arquivos.gravar_json(caminho, {"antes": 1})
                    with patch(
                        "pathlib.Path.replace", side_effect=OSError("sem acesso")
                    ):
                        with self.assertRaises(OSError):
                            arquivos.gravar_json(caminho, {"depois": 2})
                    self.assertEqual(arquivos.ler_json(caminho, {}), {"antes": 1})
                    self.assertEqual(list(Path(pasta).glob("*.tmp")), [])

    def test_utf8_invalido_nao_e_apagado(self):
        with TemporaryDirectory() as pasta:
            dados = Path(pasta) / "invalido.json"
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    dados.write_bytes(b"\xff\xfe")
                    processo = executar(
                        projeto / "solucao/main.py", pasta, "0\n", dados
                    )
                    self.assertEqual(processo.returncode, 1)
                    self.assertEqual(dados.read_bytes(), b"\xff\xfe")

    def test_ajuda_dos_cinco_programas(self):
        with TemporaryDirectory() as pasta:
            for projeto in PROJETOS:
                with self.subTest(projeto=projeto.name):
                    processo = subprocess.run(
                        [sys.executable, str(projeto / "solucao/main.py"), "--help"],
                        cwd=pasta,
                        text=True,
                        encoding="utf-8",
                        capture_output=True,
                        timeout=15,
                        env=dict(os.environ, PYTHONUTF8="1"),
                    )
                    self.assertEqual(processo.returncode, 0)
                    self.assertIn("--dados", processo.stdout)


if __name__ == "__main__":
    unittest.main()
