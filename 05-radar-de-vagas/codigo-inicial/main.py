from tarefas import apresentar_tarefa


def main():
    print("Radar de Vagas | construa seu CRUD")
    while True:
        try:
            print(
                "1 Cadastrar | 2 Consultar | 3 Atualizar | 4 Excluir | 5 Estatísticas/CSV | 0 Sair"
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
