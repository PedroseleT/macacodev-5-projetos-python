"""Execute pela raiz ou por caminho absoluto: python scripts/testar.py."""

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def main():
    if sys.version_info < (3, 11):
        print("Esta trilha requer Python 3.11 ou superior.")
        return 1
    suite = unittest.TestSuite()
    for projeto in sorted(RAIZ.glob("[0-9][0-9]-*")):
        if projeto.is_dir():
            suite.addTests(unittest.TestLoader().discover(str(projeto / "testes")))
    suite.addTests(unittest.TestLoader().discover(str(RAIZ / "testes")))
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    print(
        f"\nTotal: {resultado.testsRun} | "
        f"Falhas: {len(resultado.failures)} | Erros: {len(resultado.errors)} | "
        f"Ignorados: {len(resultado.skipped)}"
    )
    return 0 if resultado.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
