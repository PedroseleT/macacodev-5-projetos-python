from .arquivos import gravar_json, gravar_texto, ler_json
from .dominio import (
    cadastrar_cliente,
    criar_item,
    criar_orcamento,
    formatar_orcamento,
    novo_estado,
    validar_estado,
)


def exportar(estado, identificador, caminho):
    destino = caminho.parent / "orcamentos" / f"orcamento-{identificador:04d}.txt"
    gravar_texto(destino, formatar_orcamento(estado, identificador))
    print(f"Texto salvo em: {destino}")


def executar(caminho):
    try:
        estado = ler_json(caminho, novo_estado())
        validar_estado(estado)
    except (OSError, ValueError, UnicodeError) as erro:
        print(f"Não foi possível abrir os orçamentos: {erro}")
        return 1
    print("OrçaDev | valores em reais, sem separador de milhar")
    while True:
        try:
            print(
                "\n1 Cliente | 2 Novo orçamento | 3 Listar | 4 Consultar/exportar | 0 Sair"
            )
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return 0
            if opcao == "1":
                novo = cadastrar_cliente(estado, input("Nome do cliente: "))
                gravar_json(caminho, novo)
                estado = novo
                print(f"Cliente salvo com ID {estado['clientes'][-1]['id']}.")
            elif opcao == "2":
                if not estado["clientes"]:
                    print("Cadastre um cliente primeiro.")
                    continue
                for cliente in estado["clientes"]:
                    print(f"{cliente['id']} | {cliente['nome']}")
                cliente_id = int(input("ID do cliente: "))
                quantidade = int(input("Quantos serviços (1 a 100)? "))
                if not 1 <= quantidade <= 100:
                    raise ValueError("Escolha de 1 a 100 serviços.")
                itens = []
                for numero in range(1, quantidade + 1):
                    print(f"Serviço {numero}")
                    descricao = input("Descrição: ")
                    unidades = input("Quantidade inteira: ")
                    preco = input("Preço unitário: ")
                    itens.append(criar_item(descricao, unidades, preco))
                desconto = input("Desconto em reais (Enter = 0): ").strip() or "0"
                novo = criar_orcamento(estado, cliente_id, itens, desconto)
                gravar_json(caminho, novo)
                estado = novo
                identificador = estado["orcamentos"][-1]["id"]
                print("Orçamento salvo no JSON.")
                print(formatar_orcamento(estado, identificador))
                exportar(estado, identificador, caminho)
            elif opcao == "3":
                if not estado["orcamentos"]:
                    print("Nenhum orçamento salvo.")
                for item in estado["orcamentos"]:
                    print(
                        f"{item['id']} | cliente {item['cliente_id']} | {item['data']}"
                    )
            elif opcao == "4":
                identificador = int(input("ID do orçamento: "))
                print(formatar_orcamento(estado, identificador))
                exportar(estado, identificador, caminho)
            else:
                print("Opção inválida.")
        except (OSError, ValueError) as erro:
            print(
                f"Operação não concluída: {erro}. Se o JSON já foi salvo, tente exportar novamente."
            )
        except (EOFError, KeyboardInterrupt):
            print("\nOrçamentos já salvos foram preservados.")
            return 0
