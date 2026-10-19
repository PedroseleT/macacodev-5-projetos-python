# 4. Aprenda com os erros

## “TypeError: ... str ... int”

`input` devolve texto. Comparar ou somar esse texto com números não converte o valor
automaticamente. Observe `print(type(quantidade), repr(quantidade))`. Converta em
uma função de validação e trate `ValueError` quando o texto não for um número.
Não use `eval`: você precisa de um número, não de executar código digitado.

## “ValueError: day is out of range for month”

A string parece uma data, mas aquele dia não existe. O calendário é mais complexo
do que checar se tem dez caracteres. Use o parser de datas e transforme a exceção
em uma mensagem compreensível. Um `try` ao redor do menu permite repetir a operação;
isso não significa colocar um `except Exception` escondendo qualquer defeito.

## A banana mudou de identidade

Se você usa a posição da lista como ID, remover o primeiro item muda todas as
referências. Imprima a lista antes e depois de `pop`. Separe identidade da posição
e teste o fluxo cadastrar → remover → cadastrar.

## O arquivo existe, mas “perdeu tudo”

Um erro de JSON não é uma lista vazia. Trocar qualquer falha por `[]` faz o próximo
salvamento apagar o histórico. A referência interrompe a abertura e preserva o
arquivo inválido. Leia o traceback: `JSONDecodeError` informa linha e coluna.
Faça backup antes de corrigir aspas, vírgulas ou chaves manualmente.

## Um teste para uma descoberta

Reproduza o erro com o menor registro possível. Escreva o resultado esperado, faça
a correção e execute novamente. Para datas, passe uma data fixa à função. Para
arquivos, use `TemporaryDirectory` para não misturar testes com inventário real.

Confira também `NaN`: `float("NaN")` não dá erro, mas não representa quantidade
útil. Por isso a referência usa `math.isfinite`. Registre essa descoberta no seu
caderno e teste uma entrada infinita antes de [finalizar](05-finalizacao.md).
