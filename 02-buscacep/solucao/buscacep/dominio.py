"""Histórico registra somente consultas válidas, sem alterar o estado recebido."""

from copy import deepcopy
from datetime import datetime, timezone

from .servico import interpretar_resposta


def novo_estado():
    return {"versao": 1, "consultas": []}


def validar_estado(estado):
    if (
        not isinstance(estado, dict)
        or type(estado.get("versao")) is not int
        or estado["versao"] != 1
        or not isinstance(estado.get("consultas"), list)
    ):
        raise ValueError("Histórico inválido ou versão não reconhecida.")
    for consulta in estado["consultas"]:
        if not isinstance(consulta, dict):
            raise ValueError("Consulta inválida no histórico.")
        interpretar_resposta(consulta.get("endereco"))
        try:
            data = datetime.fromisoformat(consulta.get("consultado_em", ""))
        except (ValueError, TypeError) as erro:
            raise ValueError("Data de consulta inválida.") from erro
        if data.tzinfo is None:
            raise ValueError("Data de consulta deve conter fuso horário.")


def registrar(estado, endereco, instante=None):
    endereco = interpretar_resposta(endereco)
    novo = deepcopy(estado)
    novo["consultas"].append(
        {
            "endereco": endereco,
            "consultado_em": instante or datetime.now(timezone.utc).isoformat(),
        }
    )
    validar_estado(novo)
    return novo
