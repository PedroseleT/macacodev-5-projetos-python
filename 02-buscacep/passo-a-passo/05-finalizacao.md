# 5. Evolua sozinho

Execute uma consulta válida, uma inválida e outra válida. Saia, abra sem consultar
a API e leia o histórico. Você consegue explicar quais operações usam rede e
quais usam disco? Essa distinção será útil em praticamente qualquer aplicação.

Antes de consultar a referência inteira, descreva `normalizar_cep` e
`interpretar_resposta` em palavras. Uma cuida da entrada local; a outra verifica
um sistema externo. Trocar o transporte por um simulador não muda essas regras.

Escolha uma melhoria de [desafios.md](../desafios.md). Comece escrevendo a regra
e um caso de teste. Um cache, por exemplo, economiza rede, mas pode ficar antigo:
se você escolher esse desafio, mostre ao usuário quando o endereço veio do histórico.
Não apresente cache como consulta atualizada.

Prepare uma demonstração com endereço público de referência, não com o endereço
da sua casa. Documente timeout, dependência externa e caminho do histórico. Um
portfólio sério explica limitações em vez de prometer que a API nunca falha.

Marque o [checklist](../checklist.md) e registre um commit com o teste acrescentado.
No próximo projeto, os dados voltarão a ser locais, mas uma operação com dinheiro
exigirá cuidado diferente: [OrçaDev](../../03-orcadev/README.md).
