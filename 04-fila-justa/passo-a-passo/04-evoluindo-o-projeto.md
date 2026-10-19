# 4. Aprenda com os erros

## A fila virou pilha

`pop()` sem índice remove o último elemento. Isso chama a chegada mais recente,
comportamento LIFO de uma pilha. Observe uma lista de três senhas e compare `pop()`
com `pop(0)`. Guarde FIFO e LIFO como comportamentos que você consegue demonstrar,
não apenas siglas.

## “IndexError: pop from empty list”

A condição foi checada tarde demais. Faça a decisão antes de remover. Escreva
um teste de fila vazia que confirme a mensagem e a preservação do estado. Não
capture IndexError para fingir que a chamada deu certo.

## Depois de reiniciar, três prioritárias passam

Você provavelmente salvou filas, mas esqueceu o contador. Compare o JSON salvo
com todos os campos que a decisão usa. Uma regra distribuída em variáveis locais
do menu desaparece quando o processo termina. Estado persistente precisa ser explícito.

## A mesma senha aparece duas vezes

Uma transição pode ter copiado para o destino sem remover da origem, ou o arquivo
foi editado. Verifique unicidade entre filas, ativa e histórico. O mesmo ID não
pode ocupar dois estados. Crie um JSON de teste duplicado e confirme rejeição.

## Chamada não significa conclusão

Se o total aumenta ao chamar, mas o usuário ainda está sendo atendido, a estatística
está nomeada incorretamente. Use `concluidos`, `aguardando` e `em_atendimento` para
expressar as coisas diferentes. Desenhe uma tabela com uma senha em cada estado
e confira as contagens antes de [evoluir](05-finalizacao.md).
