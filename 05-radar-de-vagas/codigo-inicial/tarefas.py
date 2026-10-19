"""Construa um CRUD pequeno antes de conectar todas as opções."""


def apresentar_tarefa(opcao):
    return {
        "1": "Crie um registro com ID, empresa, cargo, link, data e status.",
        "2": "Liste os registros e filtre por status ou parte da empresa.",
        "3": "Localize por ID e valide o novo valor antes de atualizar.",
        "4": "Confirme a exclusão e preserve o próximo ID.",
        "5": "Conte por status e exporte usando csv.DictWriter.",
    }.get(opcao, "Opção inválida.")
