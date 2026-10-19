"""Tente calcular valores antes de criar o documento completo."""


def apresentar_tarefa(opcao):
    return {
        "1": "Crie uma lista de clientes com IDs e nomes validados.",
        "2": "Monte serviços com descrição, quantidade e Decimal para o preço.",
        "3": "Calcule subtotal - desconto e consulte os orçamentos salvos.",
        "4": "Formate um orçamento como string antes de gravá-lo em TXT.",
    }.get(opcao, "Opção inválida.")
