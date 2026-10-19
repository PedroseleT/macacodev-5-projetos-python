"""Arquivos UTF-8: erro de leitura nunca significa apagar os dados."""

import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def ler_json(caminho, padrao):
    caminho = Path(caminho)
    try:
        conteudo = caminho.read_text(encoding="utf-8")
    except FileNotFoundError:
        return padrao
    try:
        return json.loads(conteudo)
    except (json.JSONDecodeError, UnicodeError) as erro:
        raise ValueError(
            "JSON inválido; restaure um backup antes de continuar."
        ) from erro


def gravar_texto(caminho, texto):
    """Substitui o destino só depois de escrever um temporário no mesmo diretório."""
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = None
    try:
        with NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="",
            dir=caminho.parent,
            prefix=".macacodev-",
            suffix=".tmp",
            delete=False,
        ) as arquivo:
            temporario = Path(arquivo.name)
            arquivo.write(texto)
            arquivo.flush()
            os.fsync(arquivo.fileno())
        temporario.replace(caminho)
    finally:
        if temporario is not None:
            temporario.unlink(missing_ok=True)


def gravar_json(caminho, dados):
    texto = json.dumps(dados, ensure_ascii=False, indent=2, allow_nan=False)
    gravar_texto(caminho, texto + "\n")
