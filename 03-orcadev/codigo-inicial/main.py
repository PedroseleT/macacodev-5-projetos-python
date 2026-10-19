from tarefas import apresentar_tarefa


def main():
    print("OrçaDev | construa seu primeiro orçamento")
    while True:
        try:
            print("1 Cliente | 2 Serviços | 3 Totais e histórico | 4 Texto | 0 Sair")
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return
            print(apresentar_tarefa(opcao))
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima tentativa!")
            return


if __name__ == "__main__":
    main()
