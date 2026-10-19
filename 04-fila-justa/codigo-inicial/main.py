from tarefas import apresentar_tarefa


def main():
    print("Fila Justa | laboratório de filas e estados")
    while True:
        try:
            print("1 Comum | 2 Prioritária | 3 Fila | 4 Chamar | 5 Concluir | 0 Sair")
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return
            print(apresentar_tarefa(opcao))
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima tentativa!")
            return


if __name__ == "__main__":
    main()
