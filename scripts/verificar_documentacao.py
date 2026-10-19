"""Confere destinos relativos de links Markdown, sem depender da internet."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

RAIZ = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def problemas_de_links(raiz):
    erros = []
    quantidade = 0
    for documento in sorted(raiz.rglob("*.md")):
        if any(
            parte in {".git", ".venv", "dados", "exportacoes"}
            for parte in documento.parts
        ):
            continue
        conteudo = documento.read_text(encoding="utf-8")
        for destino in LINK.findall(conteudo):
            destino = destino.strip("<>")
            url = urlsplit(destino)
            if url.scheme or destino.startswith("#"):
                continue
            quantidade += 1
            caminho = (documento.parent / unquote(url.path)).resolve()
            if not caminho.is_relative_to(raiz.resolve()) or not caminho.exists():
                erros.append(f"{documento.relative_to(raiz)} -> {destino}")
    return quantidade, erros


def main():
    quantidade, erros = problemas_de_links(RAIZ)
    for erro in erros:
        print("Link inválido:", erro)
    print(f"Links locais verificados: {quantidade} | Inválidos: {len(erros)}")
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(main())
