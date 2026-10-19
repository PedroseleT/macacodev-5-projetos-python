from copy import deepcopy
from datetime import datetime, timezone

TIPOS = ("comum", "prioritaria")


def novo_estado():
    return {
        "versao": 1,
        "proximo_numero": 1,
        "prioritarios_seguidos": 0,
        "comum": [],
        "prioritaria": [],
        "em_atendimento": None,
        "historico": [],
    }


def instante_valido(valor=None):
    if valor is None:
        return datetime.now(timezone.utc).isoformat()
    if not isinstance(valor, str):
        raise ValueError("Instante deve ser texto ISO com fuso.")
    try:
        data = datetime.fromisoformat(valor)
    except ValueError as erro:
        raise ValueError("Instante inválido.") from erro
    if data.tzinfo is None:
        raise ValueError("Instante deve conter fuso horário.")
    return valor


def gerar_senha(estado, tipo, instante=None):
    if tipo not in TIPOS:
        raise ValueError("Categoria deve ser comum ou prioritaria.")
    novo = deepcopy(estado)
    novo[tipo].append(
        {
            "numero": novo["proximo_numero"],
            "tipo": tipo,
            "gerada_em": instante_valido(instante),
        }
    )
    novo["proximo_numero"] += 1
    return novo


def chamar_proxima(estado, instante=None):
    if estado["em_atendimento"] is not None:
        raise ValueError("Conclua o atendimento atual antes de chamar outro.")
    if not estado["comum"] and not estado["prioritaria"]:
        raise ValueError("Fila vazia.")
    novo = deepcopy(estado)
    preferir_prioritaria = bool(novo["prioritaria"]) and (
        not novo["comum"] or novo["prioritarios_seguidos"] < 2
    )
    tipo = "prioritaria" if preferir_prioritaria else "comum"
    senha = novo[tipo].pop(0)
    senha["chamada_em"] = instante_valido(instante)
    novo["em_atendimento"] = senha
    novo["prioritarios_seguidos"] = (
        min(2, novo["prioritarios_seguidos"] + 1) if tipo == "prioritaria" else 0
    )
    return novo


def concluir(estado, instante=None):
    if estado["em_atendimento"] is None:
        raise ValueError("Nenhum atendimento em andamento.")
    novo = deepcopy(estado)
    senha = novo["em_atendimento"]
    senha["concluida_em"] = instante_valido(instante)
    novo["historico"].append(senha)
    novo["em_atendimento"] = None
    return novo


def rotulo(senha):
    prefixo = "P" if senha["tipo"] == "prioritaria" else "C"
    return f"{prefixo}{senha['numero']:04d}"


def estatisticas(estado):
    concluidos = estado["historico"]
    return {
        "concluidos": len(concluidos),
        "comuns_concluidos": sum(s["tipo"] == "comum" for s in concluidos),
        "prioritarios_concluidos": sum(s["tipo"] == "prioritaria" for s in concluidos),
        "aguardando": len(estado["comum"]) + len(estado["prioritaria"]),
        "em_atendimento": int(estado["em_atendimento"] is not None),
    }


def validar_estado(estado):
    if (
        not isinstance(estado, dict)
        or type(estado.get("versao")) is not int
        or estado["versao"] != 1
    ):
        raise ValueError("Arquivo de fila inválido ou versão desconhecida.")
    if (
        type(estado.get("proximo_numero")) is not int
        or estado["proximo_numero"] < 1
        or type(estado.get("prioritarios_seguidos")) is not int
        or not 0 <= estado["prioritarios_seguidos"] <= 2
    ):
        raise ValueError("Contadores inválidos.")
    numeros = set()
    for categoria in (*TIPOS, "historico", "em_atendimento"):
        if categoria == "em_atendimento":
            if categoria not in estado:
                raise ValueError("Estado de atendimento ausente.")
            registros = [] if estado[categoria] is None else [estado[categoria]]
        else:
            registros = estado.get(categoria)
            if not isinstance(registros, list):
                raise ValueError("Fila ou histórico inválido.")
        ordem = []
        for senha in registros:
            if (
                not isinstance(senha, dict)
                or type(senha.get("numero")) is not int
                or senha["numero"] < 1
                or senha.get("tipo") not in TIPOS
            ):
                raise ValueError("Senha inválida.")
            numero = senha["numero"]
            if numero in numeros or numero >= estado["proximo_numero"]:
                raise ValueError("Senha duplicada ou contador incompatível.")
            numeros.add(numero)
            ordem.append(numero)
            if categoria in TIPOS and senha["tipo"] != categoria:
                raise ValueError("Senha está na fila errada.")
            for campo in (
                ["gerada_em"]
                + (
                    ["chamada_em"]
                    if categoria in ("historico", "em_atendimento")
                    else []
                )
                + (["concluida_em"] if categoria == "historico" else [])
            ):
                if not isinstance(senha.get(campo), str):
                    raise ValueError("Instante obrigatório ausente.")
                instante_valido(senha[campo])
        if categoria in TIPOS and ordem != sorted(ordem):
            raise ValueError("Ordem de chegada da categoria foi alterada.")
