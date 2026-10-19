from .arquivos import gravar_json, ler_json
from .dominio import (
    STATUS,
    atualizar,
    cadastrar,
    estatisticas,
    excluir,
    filtrar,
    localizar,
    novo_estado,
    pesquisar,
    validar_estado,
)
from .exportacao import exportar_csv


def escolher_status():
    for numero, status in enumerate(STATUS, 1):
        print(f"{numero} {status}")
    numero = int(input("Número do status: "))
    if not 1 <= numero <= len(STATUS):
        raise ValueError("Número de status inválido.")
    return STATUS[numero - 1]


def mostrar(registros):
    if not registros:
        print("Nenhuma candidatura nesta consulta.")
    for item in registros:
        print(
            f"{item['id']} | {item['empresa']} | {item['cargo']} | {item['status']}"
            f" | {item['data_candidatura'] or 'ainda não enviada'}\n  {item['link']}"
        )


def executar(caminho):
    try:
        estado = ler_json(caminho, novo_estado())
        validar_estado(estado)
    except (OSError, ValueError, UnicodeError) as erro:
        print(f"Não foi possível abrir as candidaturas: {erro}")
        return 1
    print("Radar de Vagas Dev | cadastro manual, sem busca automática")
    while True:
        try:
            print(
                "\n1 Cadastrar | 2 Listar | 3 Filtrar status | 4 Pesquisar empresa | 5 Atualizar | 6 Excluir | 7 Estatísticas | 8 CSV | 0 Sair"
            )
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return 0
            novo = None
            if opcao == "1":
                empresa = input("Empresa: ")
                cargo = input("Cargo: ")
                link = input("Link completo da vaga: ")
                status = escolher_status()
                data = input(
                    "Data candidatura DD/MM/AAAA (vazio só para Interesse): "
                ).strip()
                novo = cadastrar(estado, empresa, cargo, link, data, status)
            elif opcao == "2":
                mostrar(estado["candidaturas"])
            elif opcao == "3":
                mostrar(filtrar(estado, escolher_status()))
            elif opcao == "4":
                mostrar(pesquisar(estado, input("Parte do nome da empresa: ")))
            elif opcao == "5":
                identificador = int(input("ID da candidatura: "))
                atual = localizar(estado, identificador)
                campo = input(
                    "Campo (empresa, cargo, link, data_candidatura, status): "
                ).strip()
                if campo == "status":
                    valor = escolher_status()
                    alteracoes = {campo: valor}
                    if atual["data_candidatura"] is None and valor != "Interesse":
                        alteracoes["data_candidatura"] = input(
                            "Data candidatura DD/MM/AAAA: "
                        )
                else:
                    alteracoes = {campo: input("Novo valor: ")}
                novo = atualizar(estado, identificador, alteracoes)
            elif opcao == "6":
                identificador = int(input("ID para excluir: "))
                mostrar([localizar(estado, identificador)])
                if input("Digite SIM para excluir: ").strip().upper() == "SIM":
                    novo = excluir(estado, identificador)
                else:
                    print("Exclusão cancelada.")
            elif opcao == "7":
                resumo = estatisticas(estado)
                print(f"Total: {resumo['total']}")
                for status, quantidade in resumo["por_status"].items():
                    print(f"{status}: {quantidade}")
            elif opcao == "8":
                destino = caminho.parent / "exportacoes" / "candidaturas.csv"
                exportar_csv(estado, destino)
                print(f"CSV salvo em: {destino}")
            else:
                print("Opção inválida.")
            if novo is not None:
                gravar_json(caminho, novo)
                estado = novo
                print("Alteração salva.")
        except (OSError, ValueError) as erro:
            print(f"Não foi possível concluir: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nCandidaturas já salvas foram preservadas.")
            return 0
