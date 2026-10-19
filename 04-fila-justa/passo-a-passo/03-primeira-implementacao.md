# 3. Construa por etapas

## A · gere e liste

Objetivo: acrescentar senhas sem sobrescrever anteriores. Conceitos: lista,
dicionário e contador. Tarefa: gere C1, P2 e C3. Esperado: listas diferentes e
números únicos. Teste categoria desconhecida e confirme que nada foi criado.
Listar não pode remover itens: percorra com `for`, não com `pop`.

## B · chame somente uma

Objetivo: mover uma senha para `em_atendimento`. Conceitos: estado e condição.
Tarefa: retire a primeira senha comum quando não há prioritária. Esperado: ela sai
da lista e aparece como ativa. Uma segunda chamada antes da conclusão deve falhar
sem alterar nenhuma lista. Teste também fila vazia.

## C · aplique a política

Objetivo: preservar prioridade sem esquecer comuns. Conceitos: contador e combinação
de condições. Tarefa: implemente a sequência 2:1. Esperado: P2, P3, C1, P5, C4 para
o exemplo do tutorial. Teste só comuns e só prioritárias. Depois faça uma comum
chegar após duas prioritárias já atendidas e confira o turno seguinte.

## D · conclua e conte

Objetivo: distinguir chamada de conclusão. Tarefa: registre instante da chamada
e da conclusão; acrescente ao histórico somente ao concluir. Esperado: uma senha
ativa não entra no total de concluídos. Teste concluir sem atendimento e confirme
mensagem explícita. Mostre contagens por categoria.

## E · recupere o estado completo

Objetivo: manter a regra após fechar o terminal. Conceitos: JSON e validação.
Tarefa: salve durante um atendimento, recarregue e conclua. Esperado: nenhuma senha
se perde nem volta ao começo da fila. Teste também a recuperação após duas chamadas
prioritárias. Dados corrompidos devem interromper abertura, não zerar o balcão.

Imprima cópias do estado durante testes manuais para observar as transições. Depois
remova prints de depuração e siga para [investigar erros](04-evoluindo-o-projeto.md).
