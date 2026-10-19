import argparse
from pathlib import Path

from filajusta.terminal import executar


def main():
    parser = argparse.ArgumentParser(description="Fila Justa - MacacoDev")
    parser.add_argument(
        "--dados",
        type=Path,
        default=(Path(__file__).resolve().parents[1] / "dados" / "fila.json"),
    )
    return executar(parser.parse_args().dados)


if __name__ == "__main__":
    raise SystemExit(main())
