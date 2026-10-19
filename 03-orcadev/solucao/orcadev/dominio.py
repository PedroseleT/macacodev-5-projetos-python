from copy import deepcopy
from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENTAVO = Decimal("0.01")


def novo_estado():
    return {
        "versao": 1,
        "proximo_cliente": 1,
        "proximo_orcamento": 1,
        "clientes": [],
        "orcamentos": [],
    }


def texto_valido(valor):
    if not isinstance(valor, str) or not 1 <= len(valor.strip()) <= 200:
        raise ValueError("Texto deve ter de 1 a 200 caracteres.")
    if "\n" in valor or "\r" in valor:
        raise ValueError("Use somente uma linha por campo.")
    return valor.strip()


def dinheiro(valor):
    if isinstance(valor, bool) or not isinstance(valor, (str, int, Decimal)):
        raise ValueError("Informe dinheiro como texto, sem usar float.")
    try:
        numero = Decimal(str(valor).strip().replace(",", "."))
    except InvalidOperation as erro:
        raise ValueError("Valor monetário inválido.") from erro
    if not numero.is_finite() or not 0 <= numero <= Decimal("1000000000"):
        raise ValueError("Valor deve estar entre zero e um bilhão.")
    if numero != numero.quantize(CENTAVO, rounding=ROUND_HALF_UP):
        raise ValueError("Informe no máximo duas casas decimais.")
    return numero.quantize(CENTAVO, rounding=ROUND_HALF_UP)


def quantidade_valida(valor):
    if isinstance(valor, bool) or not isinstance(valor, (str, int)):
        raise ValueError("Quantidade deve ser inteira e positiva.")
    try:
        quantidade = int(valor)
    except ValueError as erro:
        raise ValueError("Quantidade deve ser inteira e positiva.") from erro
    if not 1 <= quantidade <= 1_000_000:
        raise ValueError("Quantidade deve estar entre 1 e um milhão.")
    return quantidade


def criar_item(descricao, quantidade, preco):
    valor = dinheiro(preco)
    if valor == 0:
        raise ValueError("Preço unitário deve ser maior que zero.")
    return {
        "descricao": texto_valido(descricao),
        "quantidade": quantidade_valida(quantidade),
        "preco_unitario": str(valor),
    }


def calcular_totais(itens, desconto="0"):
    if not isinstance(itens, list) or not 1 <= len(itens) <= 100:
        raise ValueError("Orçamento deve ter de 1 a 100 serviços.")
    subtotal = Decimal("0.00")
    for item in itens:
        if not isinstance(item, dict):
            raise ValueError("Serviço inválido.")
        normalizado = criar_item(
            item.get("descricao"), item.get("quantidade"), item.get("preco_unitario")
        )
        subtotal += dinheiro(normalizado["preco_unitario"]) * normalizado["quantidade"]
    desconto = dinheiro(desconto)
    if desconto > subtotal:
        raise ValueError("Desconto não pode superar o subtotal.")
    return {"subtotal": subtotal, "desconto": desconto, "total": subtotal - desconto}


def cadastrar_cliente(estado, nome):
    novo = deepcopy(estado)
    novo["clientes"].append({"id": novo["proximo_cliente"], "nome": texto_valido(nome)})
    novo["proximo_cliente"] += 1
    return novo


def criar_orcamento(estado, cliente_id, itens, desconto="0", hoje=None):
    if type(cliente_id) is not int or not any(
        c["id"] == cliente_id for c in estado["clientes"]
    ):
        raise ValueError("Cliente não encontrado. Cadastre-o primeiro.")
    totais = calcular_totais(itens, desconto)
    novo = deepcopy(estado)
    novo["orcamentos"].append(
        {
            "id": novo["proximo_orcamento"],
            "cliente_id": cliente_id,
            "data": (hoje or date.today()).isoformat(),
            "itens": [
                criar_item(i["descricao"], i["quantidade"], i["preco_unitario"])
                for i in itens
            ],
            "desconto": str(totais["desconto"]),
        }
    )
    novo["proximo_orcamento"] += 1
    return novo


def validar_estado(estado):
    if (
        not isinstance(estado, dict)
        or type(estado.get("versao")) is not int
        or estado["versao"] != 1
    ):
        raise ValueError("Arquivo de orçamentos inválido ou versão desconhecida.")
    for chave, proximo in [
        ("clientes", "proximo_cliente"),
        ("orcamentos", "proximo_orcamento"),
    ]:
        registros = estado.get(chave)
        if not isinstance(registros, list) or type(estado.get(proximo)) is not int:
            raise ValueError("Coleção ou próximo ID inválido.")
        ids = []
        for item in registros:
            if (
                not isinstance(item, dict)
                or type(item.get("id")) is not int
                or item["id"] < 1
            ):
                raise ValueError("Registro sem ID válido.")
            ids.append(item["id"])
        if len(ids) != len(set(ids)) or estado[proximo] <= max(ids, default=0):
            raise ValueError("IDs repetidos ou contador inválido.")
    for cliente in estado["clientes"]:
        texto_valido(cliente.get("nome"))
    clientes = {c["id"] for c in estado["clientes"]}
    for orcamento in estado["orcamentos"]:
        if (
            type(orcamento.get("cliente_id")) is not int
            or orcamento["cliente_id"] not in clientes
        ):
            raise ValueError("Orçamento referencia cliente inexistente.")
        try:
            data = date.fromisoformat(orcamento.get("data", ""))
        except (ValueError, TypeError) as erro:
            raise ValueError("Data do orçamento inválida.") from erro
        if data.isoformat() != orcamento["data"]:
            raise ValueError("Use data ISO no arquivo.")
        calcular_totais(orcamento.get("itens"), orcamento.get("desconto"))


def localizar_orcamento(estado, identificador):
    for orcamento in estado["orcamentos"]:
        if type(identificador) is int and orcamento["id"] == identificador:
            return orcamento
    raise ValueError("Orçamento não encontrado.")


def moeda(valor):
    return "R$ " + format(valor, ".2f").replace(".", ",")


def formatar_orcamento(estado, identificador):
    orcamento = localizar_orcamento(estado, identificador)
    cliente = next(c for c in estado["clientes"] if c["id"] == orcamento["cliente_id"])
    totais = calcular_totais(orcamento["itens"], orcamento["desconto"])
    linhas = [
        f"ORÇAMENTO {identificador:04d}",
        f"Cliente: {cliente['nome']}",
        f"Data: {orcamento['data']}",
        "",
        "SERVIÇOS",
    ]
    for item in orcamento["itens"]:
        preco = dinheiro(item["preco_unitario"])
        linhas.append(
            f"{item['descricao']} | {item['quantidade']} x {moeda(preco)}"
            f" = {moeda(preco * item['quantidade'])}"
        )
    linhas += [
        "",
        f"Subtotal: {moeda(totais['subtotal'])}",
        f"Desconto: {moeda(totais['desconto'])}",
        f"TOTAL: {moeda(totais['total'])}",
    ]
    return "\n".join(linhas) + "\n"
