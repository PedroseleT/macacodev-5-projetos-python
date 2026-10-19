"""Antes de automatizar, simule a política 2:1 no papel."""


def apresentar_tarefa(opcao):
    return {
        "1": "Adicione uma senha ao fim da lista comum com número único.",
        "2": "Use outra lista para a categoria prioritária, preservando chegada.",
        "3": "Mostre as duas listas sem removê-las.",
        "4": "Escolha pela política 2:1 e mova uma senha para em_atendimento.",
        "5": "Mova o atendimento atual para o histórico; depois salve o estado.",
    }.get(opcao, "Opção inválida.")
