# 2. Planeje a solução

Use duas listas, uma por categoria. `append` coloca no fim; `pop(0)` retira o
primeiro item, preservando FIFO. Essa solução é compreensível para filas pequenas.
Estruturas como `deque` podem melhorar remoção no início; não precisamos introduzi-las
antes de entender o algoritmo.

O estado também precisa de `em_atendimento`, `historico`, `proximo_numero` e
`prioritarios_seguidos`. Se salvar somente as listas, você esquecerá a pessoa que
já saiu da fila mas ainda não terminou.

## Transformações do estado

```text
gerar: criar senha e acrescentar à categoria
chamar: escolher categoria e mover a primeira para atendimento ativo
concluir: mover a ativa para histórico e deixar atendimento vazio
```

Planeje `gerar_senha`, `chamar_proxima`, `concluir` e `estatisticas`. Elas recebem
estado e devolvem novo estado ou resultado. O terminal faz input/print; o módulo
de arquivos salva. Uma falha não pode remover uma senha parcialmente.

## Como decidir a categoria

1. Se existe atendimento ativo, rejeite nova chamada.
2. Se ambas as listas estão vazias, informe fila vazia.
3. Prefira prioritária se existe e o limite de duas não foi atingido, ou se não há comum.
4. Caso contrário, retire a primeira comum e zere o contador de prioritárias.

Limite o contador a dois: uma sequência longa de prioritárias sozinhas não precisa
guardar um número enorme. Quando uma comum chegar, a informação “limite atingido”
já basta para decidir o turno.

Desenhe três operações seguidas e liste quais campos mudam em cada uma. Se conseguir
simular uma reinicialização entre chamadas, siga para [construção](03-primeira-implementacao.md).
