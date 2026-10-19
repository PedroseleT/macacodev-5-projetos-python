import csv
from io import StringIO

from .arquivos import gravar_texto


def celula_segura(valor):
    """Evita que texto de empresa/cargo seja interpretado como fórmula em planilha."""
    texto = "" if valor is None else str(valor)
    if texto.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + texto
    return texto


def gerar_csv(estado):
    saida = StringIO(newline="")
    campos = ["id", "empresa", "cargo", "link", "data_candidatura", "status"]
    escritor = csv.DictWriter(saida, fieldnames=campos, lineterminator="\n")
    escritor.writeheader()
    for candidatura in estado["candidaturas"]:
        escritor.writerow(
            {campo: celula_segura(candidatura.get(campo)) for campo in campos}
        )
    return saida.getvalue()


def exportar_csv(estado, destino):
    gravar_texto(destino, gerar_csv(estado))
