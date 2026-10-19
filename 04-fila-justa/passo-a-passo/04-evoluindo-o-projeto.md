# 4. A fila se embolou? Vamos acompanhar uma senha

Quando algo estranho acontecer, diminua o exemplo. Três senhas são mais fáceis
de acompanhar do que trinta. Anote a ordem esperada e veja onde o programa saiu
desse caminho.

## Quem chegou por último foi chamado primeiro

Confira se você usou `pop()` sem indicar a posição. Assim, Python retira o
último elemento. Para a primeira pessoa da lista, use `pop(0)`.

Experimente com uma lista pequena e observe a diferença. Não precisa decorar
uma sigla para entender quem está saindo.

## Apareceu IndexError

A mensagem `pop from empty list` diz que você tentou retirar um item de uma
lista vazia. A solução é conferir se há senhas antes de remover.

Mostre “Não há senhas aguardando” e volte ao menu. Isso é uma situação normal
de uso, não motivo para encerrar o programa.

## Depois de abrir de novo, a ordem mudou

Talvez você tenha salvo as filas, mas esquecido o contador de prioritárias.
Confira quais informações a escolha da próxima senha usa e se todas foram
guardadas no arquivo.

## A mesma senha está em dois lugares

Uma senha chamada deve sair da fila. Quando concluir, deve sair do atendimento
e ir para o histórico. Colocar no destino sem tirar da origem duplica a senha.

Use mensagens como `print(fila_comum)` e `print(em_atendimento)` antes e depois
da chamada. Acompanhe a mesma senha pelo número e retire essas mensagens extras
depois que descobrir o problema.

[Anterior: construir](03-primeira-implementacao.md) · [Próximo: fazer sua versão](05-finalizacao.md)
