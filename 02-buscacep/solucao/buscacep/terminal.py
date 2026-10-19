from .arquivos import gravar_json, ler_json
from .dominio import novo_estado, registrar, validar_estado
from .servico import consultar


def mostrar(endereco):
    print(f"CEP: {endereco['cep']}")
    print(f"Logradouro: {endereco['logradouro'] or '(não informado)'}")
    print(f"Bairro: {endereco['bairro'] or '(não informado)'}")
    print(f"Cidade: {endereco['localidade']} | Estado: {endereco['uf']}")


def executar(caminho):
    try:
        estado = ler_json(caminho, novo_estado())
        validar_estado(estado)
    except (OSError, ValueError, UnicodeError) as erro:
        print(f"Não foi possível abrir o histórico: {erro}")
        return 1
    print("BuscaCEP Inteligente | serviço público ViaCEP")
    while True:
        try:
            print("\n1 Consultar CEP | 2 Histórico | 0 Sair")
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return 0
            if opcao == "1":
                endereco = consultar(input("CEP: "))
                mostrar(endereco)
                novo = registrar(estado, endereco)
                gravar_json(caminho, novo)
                estado = novo
                print("Consulta salva no histórico.")
            elif opcao == "2":
                if not estado["consultas"]:
                    print("Nenhuma consulta salva.")
                for consulta in estado["consultas"]:
                    print(f"\nConsultado em: {consulta['consultado_em']}")
                    mostrar(consulta["endereco"])
            else:
                print("Opção inválida.")
        except (OSError, ValueError) as erro:
            print(f"Operação não concluída ou histórico não salvo: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nAté a próxima consulta!")
            return 0
