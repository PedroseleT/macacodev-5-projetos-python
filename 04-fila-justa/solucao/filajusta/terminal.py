from .arquivos import gravar_json, ler_json
from .dominio import (
    chamar_proxima,
    concluir,
    estatisticas,
    gerar_senha,
    novo_estado,
    rotulo,
    validar_estado,
)


def mostrar_fila(estado):
    for tipo in ("prioritaria", "comum"):
        print(f"{tipo}: " + (", ".join(rotulo(s) for s in estado[tipo]) or "vazia"))
    atual = estado["em_atendimento"]
    print("Em atendimento: " + (rotulo(atual) if atual else "nenhuma"))


def executar(caminho):
    try:
        estado = ler_json(caminho, novo_estado())
        validar_estado(estado)
    except (OSError, ValueError, UnicodeError) as erro:
        print(f"Não foi possível abrir a fila: {erro}")
        return 1
    print("Fila Justa | 2 prioritárias : 1 comum quando ambas aguardam")
    print("Política didática; não certifica cumprimento de legislação.")
    while True:
        try:
            print(
                "\n1 Comum | 2 Prioritária | 3 Fila | 4 Chamar | 5 Concluir | 6 Histórico | 7 Estatísticas | 0 Sair"
            )
            opcao = input("Escolha: ").strip()
            if opcao == "0":
                return 0
            novo = None
            mensagem = ""
            if opcao in ("1", "2"):
                tipo = "comum" if opcao == "1" else "prioritaria"
                novo = gerar_senha(estado, tipo)
                mensagem = "Gerada: " + rotulo(novo[tipo][-1])
            elif opcao == "3":
                mostrar_fila(estado)
            elif opcao == "4":
                novo = chamar_proxima(estado)
                mensagem = "Chamada: " + rotulo(novo["em_atendimento"])
            elif opcao == "5":
                novo = concluir(estado)
                mensagem = "Atendimento concluído."
            elif opcao == "6":
                if not estado["historico"]:
                    print("Nenhum atendimento concluído.")
                for senha in estado["historico"]:
                    print(
                        f"{rotulo(senha)} | chamada {senha['chamada_em']} | conclusão {senha['concluida_em']}"
                    )
                if estado["em_atendimento"]:
                    print("Chamada em andamento: " + rotulo(estado["em_atendimento"]))
            elif opcao == "7":
                for nome, quantidade in estatisticas(estado).items():
                    print(f"{nome}: {quantidade}")
            else:
                print("Opção inválida.")
            if novo is not None:
                gravar_json(caminho, novo)
                estado = novo
                print(mensagem + " Estado salvo.")
        except (OSError, ValueError) as erro:
            print(f"Não foi possível concluir: {erro}")
        except (EOFError, KeyboardInterrupt):
            print("\nFila salva preservada.")
            return 0
