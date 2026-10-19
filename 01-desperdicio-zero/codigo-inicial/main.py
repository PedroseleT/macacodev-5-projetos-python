"""Ponto de partida executável. Siga o passo a passo para implementar as tarefas."""

from tarefas import apresentar_tarefa


def main():
    print("Desperdício Zero | sua implementação começa aqui")
    while True:
        try:
            print(
                "1 Cadastrar | 2 Listar | 3 Próximos | 4 Vencidos | 5 Remover | 0 Sair"
            )
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return
            print(apresentar_tarefa(opcao))
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima tentativa!")
            return


if __name__ == "__main__":
    main()
