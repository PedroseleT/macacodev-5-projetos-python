"""Implemente uma tarefa de cada vez; não importe a solução aqui."""


def apresentar_tarefa(opcao):
    tarefas = {
        "1": "Crie cadastrar(): receba nome, quantidade e validade; retorne um dicionário.",
        "2": "Guarde alimentos em uma lista e percorra cada item com for.",
        "3": "Converta a validade em date e calcule quantos dias faltam.",
        "4": "Separe datas anteriores a hoje das datas iguais a hoje.",
        "5": "Remova pelo ID, não pela posição exibida na lista.",
    }
    return tarefas.get(opcao, "Opção inválida.")
