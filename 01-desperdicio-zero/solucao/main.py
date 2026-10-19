"""Execute: python solucao/main.py [--dados outro.json]."""

import argparse
from pathlib import Path

from desperdicio.terminal import executar


def main():
    parser = argparse.ArgumentParser(description="Desperdício Zero - MacacoDev")
    parser.add_argument(
        "--dados",
        type=Path,
        default=(Path(__file__).resolve().parents[1] / "dados" / "alimentos.json"),
    )
    return executar(parser.parse_args().dados)


if __name__ == "__main__":
    raise SystemExit(main())
