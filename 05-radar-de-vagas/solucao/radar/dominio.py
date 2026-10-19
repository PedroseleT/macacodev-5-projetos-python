from copy import deepcopy
from datetime import date, datetime, timezone
from urllib.parse import urlsplit

STATUS = (
    "Interesse",
    "Candidatura enviada",
    "Entrevista",
    "Teste técnico",
    "Proposta",
    "Aprovado",
    "Rejeitado",
)
CAMPOS = {"empresa", "cargo", "link", "data_candidatura", "status"}


def novo_estado():
    return {"versao": 1, "proximo_id": 1, "candidaturas": []}


def texto_valido(valor):
    if not isinstance(valor, str) or not 1 <= len(valor.strip()) <= 160:
        raise ValueError("Empresa/cargo deve ter de 1 a 160 caracteres.")
    if any(ord(c) < 32 for c in valor):
        raise ValueError("Empresa/cargo deve ocupar uma linha, sem controles.")
    return valor.strip()


def link_valido(valor):
    if not isinstance(valor, str) or len(valor) > 2048:
        raise ValueError("Link inválido ou muito longo.")
    valor = valor.strip()
    if any(c.isspace() or ord(c) < 32 for c in valor):
        raise ValueError("Link não pode conter espaços.")
    try:
        partes = urlsplit(valor)
        porta = partes.port
    except ValueError as erro:
        raise ValueError("Link malformado.") from erro
    if (
        partes.scheme not in ("http", "https")
        or not partes.hostname
        or partes.username is not None
        or partes.password is not None
    ):
        raise ValueError("Use um link http/https completo, sem credenciais.")
    if porta is not None and not 1 <= porta <= 65535:
        raise ValueError("Porta inválida no link.")
    return valor


def status_valido(valor):
    if isinstance(valor, str):
        for status in STATUS:
            if status.casefold() == valor.strip().casefold():
                return status
    raise ValueError("Status não reconhecido; escolha um dos sete estados do menu.")


def data_de_entrada(texto):
    try:
        data = datetime.strptime(texto, "%d/%m/%Y").date()
    except (ValueError, TypeError) as erro:
        raise ValueError("Use uma data real no formato DD/MM/AAAA.") from erro
    if data.strftime("%d/%m/%Y") != texto:
        raise ValueError("Dia e mês devem ter dois dígitos.")
    return data.isoformat()


def validar_registro(registro):
    if (
        not isinstance(registro, dict)
        or type(registro.get("id")) is not int
        or registro["id"] < 1
    ):
        raise ValueError("Candidatura sem ID válido.")
    texto_valido(registro.get("empresa"))
    texto_valido(registro.get("cargo"))
    link_valido(registro.get("link"))
    status = status_valido(registro.get("status"))
    valor = registro.get("data_candidatura")
    if valor is None:
        if status != "Interesse":
            raise ValueError(
                "Informe a data da candidatura antes de mudar para esse status."
            )
    else:
        try:
            data = date.fromisoformat(valor)
        except (ValueError, TypeError) as erro:
            raise ValueError("Data de candidatura inválida no arquivo.") from erro
        if data.isoformat() != valor:
            raise ValueError("Data persistida deve usar AAAA-MM-DD.")
    for campo in ("criada_em", "atualizada_em"):
        try:
            instante = datetime.fromisoformat(registro.get(campo, ""))
        except (ValueError, TypeError) as erro:
            raise ValueError("Instante inválido no arquivo.") from erro
        if instante.tzinfo is None:
            raise ValueError("Instante deve ter fuso horário.")


def validar_estado(estado):
    if (
        not isinstance(estado, dict)
        or type(estado.get("versao")) is not int
        or estado["versao"] != 1
        or not isinstance(estado.get("candidaturas"), list)
        or type(estado.get("proximo_id")) is not int
    ):
        raise ValueError("Arquivo de candidaturas inválido ou versão desconhecida.")
    ids = set()
    for registro in estado["candidaturas"]:
        validar_registro(registro)
        if registro["id"] in ids:
            raise ValueError("ID de candidatura duplicado.")
        ids.add(registro["id"])
    if estado["proximo_id"] <= max(ids, default=0):
        raise ValueError("Contador de IDs incompatível.")


def cadastrar(estado, empresa, cargo, link, data_candidatura, status):
    instante = datetime.now(timezone.utc).isoformat()
    registro = {
        "id": estado["proximo_id"],
        "empresa": texto_valido(empresa),
        "cargo": texto_valido(cargo),
        "link": link_valido(link),
        "data_candidatura": data_de_entrada(data_candidatura)
        if data_candidatura
        else None,
        "status": status_valido(status),
        "criada_em": instante,
        "atualizada_em": instante,
    }
    validar_registro(registro)
    novo = deepcopy(estado)
    novo["candidaturas"].append(registro)
    novo["proximo_id"] += 1
    return novo


def localizar(estado, identificador):
    for item in estado["candidaturas"]:
        if type(identificador) is int and item["id"] == identificador:
            return item
    raise ValueError("Candidatura não encontrada.")


def atualizar(estado, identificador, alteracoes):
    if not isinstance(alteracoes, dict) or not alteracoes or set(alteracoes) - CAMPOS:
        raise ValueError("Escolha campos editáveis; ID e criação não podem mudar.")
    novo = deepcopy(estado)
    registro = localizar(novo, identificador)
    for campo, valor in alteracoes.items():
        if campo in ("empresa", "cargo"):
            valor = texto_valido(valor)
        elif campo == "link":
            valor = link_valido(valor)
        elif campo == "status":
            valor = status_valido(valor)
        elif campo == "data_candidatura":
            valor = data_de_entrada(valor) if valor else None
        registro[campo] = valor
    registro["atualizada_em"] = datetime.now(timezone.utc).isoformat()
    validar_registro(registro)
    return novo


def excluir(estado, identificador):
    localizar(estado, identificador)
    novo = deepcopy(estado)
    novo["candidaturas"] = [c for c in novo["candidaturas"] if c["id"] != identificador]
    return novo


def filtrar(estado, status):
    status = status_valido(status)
    return [deepcopy(c) for c in estado["candidaturas"] if c["status"] == status]


def pesquisar(estado, empresa):
    termo = texto_valido(empresa).casefold()
    return [
        deepcopy(c) for c in estado["candidaturas"] if termo in c["empresa"].casefold()
    ]


def estatisticas(estado):
    return {
        "total": len(estado["candidaturas"]),
        "por_status": {
            status: sum(c["status"] == status for c in estado["candidaturas"])
            for status in STATUS
        },
    }
