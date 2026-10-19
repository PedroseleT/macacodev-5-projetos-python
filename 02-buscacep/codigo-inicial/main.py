from tarefas import apresentar_tarefa


def main():
    print("BuscaCEP | seu laboratório de consultas")
    while True:
        try:
            print("1 Consultar | 2 Histórico | 0 Sair")
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return
            print(apresentar_tarefa(opcao))
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima tentativa!")
            return


if __name__ == "__main__":
    main()
