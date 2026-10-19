"""Interface: só adota o novo estado depois de salvar com sucesso."""

from .arquivos import gravar_json, ler_json
from .dominio import cadastrar, novo_estado, remover, situacao, validar_estado


def mostrar(alimentos):
    if not alimentos:
        print("Nenhum alimento nesta lista.")
    for item in alimentos:
        print(
            f"{item['id']} | {item['nome']} | {item['quantidade']:g} | "
            f"{item['validade']} | {situacao(item)}"
        )


def executar(caminho):
    try:
        estado = ler_json(caminho, novo_estado())
        validar_estado(estado)
    except (OSError, ValueError, UnicodeError) as erro:
        print(f"Não foi possível abrir os dados: {erro}")
        return 1
    print("Desperdício Zero | datas DD/MM/AAAA | próximos: até 3 dias")
    while True:
        try:
            print(
                "\n1 Cadastrar | 2 Listar | 3 Próximos | 4 Vencidos | 5 Remover | 0 Sair"
            )
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return 0
            novo = None
            if opcao == "1":
                nome = input("Alimento: ")
                quantidade = input("Quantidade: ")
                validade = input("Validade (DD/MM/AAAA): ")
                novo = cadastrar(estado, nome, quantidade, validade)
            elif opcao == "2":
                mostrar(estado["alimentos"])
            elif opcao in ("3", "4"):
                filtro = "proximo" if opcao == "3" else "vencido"
                mostrar([i for i in estado["alimentos"] if situacao(i) == filtro])
            elif opcao == "5":
                novo = remover(estado, int(input("ID do alimento: ")))
            else:
                print("Opção inválida. Escolha um número do menu.")
            if novo is not None:
                gravar_json(caminho, novo)
                estado = novo
                print("Alteração salva.")
        except (OSError, ValueError) as erro:
            print(f"Não foi possível concluir: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrado. Alterações já salvas foram preservadas.")
            return 0
