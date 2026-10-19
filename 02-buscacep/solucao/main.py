import argparse
from pathlib import Path

from buscacep.terminal import executar


def main():
    parser = argparse.ArgumentParser(description="BuscaCEP Inteligente - MacacoDev")
    parser.add_argument(
        "--dados",
        type=Path,
        default=(Path(__file__).resolve().parents[1] / "dados" / "historico.json"),
    )
    return executar(parser.parse_args().dados)


if __name__ == "__main__":
    raise SystemExit(main())
