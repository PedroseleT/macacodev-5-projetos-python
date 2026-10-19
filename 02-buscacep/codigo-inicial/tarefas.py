"""Comece pela validação local antes de tentar acessar a internet."""


def apresentar_tarefa(opcao):
    tarefas = {
        "1": "Implemente normalizar_cep(). Só depois conecte urllib e valide a resposta.",
        "2": "Guarde apenas endereços válidos numa lista e salve o histórico em JSON.",
    }
    return tarefas.get(opcao, "Opção inválida.")
