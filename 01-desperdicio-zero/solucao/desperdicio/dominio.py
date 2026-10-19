"""Regras sem input, print ou acesso ao disco."""

from copy import deepcopy
from datetime import date, datetime
from math import isfinite


def novo_estado():
    return {"versao": 1, "proximo_id": 1, "alimentos": []}


def nome_valido(nome):
    if not isinstance(nome, str) or not 1 <= len(nome.strip()) <= 120:
        raise ValueError("Nome deve ter de 1 a 120 caracteres.")
    return nome.strip()


def quantidade_valida(valor):
    if isinstance(valor, bool) or not isinstance(valor, (str, int, float)):
        raise ValueError("Quantidade deve ser um número positivo.")
    try:
        numero = float(str(valor).strip().replace(",", "."))
    except ValueError as erro:
        raise ValueError("Quantidade deve ser um número positivo.") from erro
    if not isfinite(numero) or not 0 < numero <= 1_000_000_000:
        raise ValueError("Quantidade deve ser maior que zero e até um bilhão.")
    return numero


def data_de_entrada(texto):
    try:
        resultado = datetime.strptime(texto, "%d/%m/%Y").date()
    except (ValueError, TypeError) as erro:
        raise ValueError("Informe uma data real no formato DD/MM/AAAA.") from erro
    if resultado.strftime("%d/%m/%Y") != texto:
        raise ValueError("Use dois dígitos para dia e mês e quatro para ano.")
    return resultado.isoformat()


def validar_estado(estado):
    if (
        not isinstance(estado, dict)
        or type(estado.get("versao")) is not int
        or estado["versao"] != 1
    ):
        raise ValueError("Formato ou versão do arquivo não reconhecido.")
    alimentos = estado.get("alimentos")
    proximo = estado.get("proximo_id")
    if not isinstance(alimentos, list) or type(proximo) is not int or proximo < 1:
        raise ValueError("Lista de alimentos ou próximo ID inválido.")
    ids = set()
    for item in alimentos:
        if not isinstance(item, dict) or type(item.get("id")) is not int:
            raise ValueError("Alimento sem ID inteiro.")
        if item["id"] < 1 or item["id"] in ids:
            raise ValueError("IDs de alimentos inválidos ou duplicados.")
        ids.add(item["id"])
        nome_valido(item.get("nome"))
        quantidade_valida(item.get("quantidade"))
        validade = item.get("validade")
        try:
            data = date.fromisoformat(validade)
        except (ValueError, TypeError) as erro:
            raise ValueError("Validade inválida no arquivo.") from erro
        if data.isoformat() != validade:
            raise ValueError("Validade deve usar AAAA-MM-DD no arquivo.")
    if ids and proximo <= max(ids):
        raise ValueError("Próximo ID precisa superar os IDs existentes.")


def cadastrar(estado, nome, quantidade, validade):
    item = {
        "id": estado["proximo_id"],
        "nome": nome_valido(nome),
        "quantidade": quantidade_valida(quantidade),
        "validade": data_de_entrada(validade),
    }
    novo = deepcopy(estado)
    novo["alimentos"].append(item)
    novo["proximo_id"] += 1
    return novo


def remover(estado, identificador):
    if type(identificador) is not int:
        raise ValueError("ID deve ser inteiro.")
    if not any(item["id"] == identificador for item in estado["alimentos"]):
        raise ValueError("Alimento não encontrado.")
    novo = deepcopy(estado)
    novo["alimentos"] = [i for i in novo["alimentos"] if i["id"] != identificador]
    return novo


def situacao(item, hoje=None, dias=3):
    """Validade igual a hoje ainda não está vencida; é próxima."""
    if type(dias) is not int or dias < 0:
        raise ValueError("Prazo deve ser um inteiro não negativo.")
    diferenca = (date.fromisoformat(item["validade"]) - (hoje or date.today())).days
    if diferenca < 0:
        return "vencido"
    return "proximo" if diferenca <= dias else "em_dia"
