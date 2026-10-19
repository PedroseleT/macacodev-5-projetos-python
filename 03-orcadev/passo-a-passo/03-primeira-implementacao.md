# 3. Construa por etapas

## A · cliente e serviço

Objetivo: representar dados sem menu. Conceitos: dicionários e validação. Tarefa:
crie um cliente com ID e um serviço com descrição, quantidade inteira e preço
Decimal. Esperado: descrição vazia e quantidade zero são rejeitadas. Teste valores
diretos; conecte `input` somente depois.

## B · calcule um subtotal

Objetivo: transformar uma lista de serviços em um resultado. Conceitos: acumulação
com `for` e Decimal. Comece com dois itens e calcule à mão. Tarefa: devolva subtotal,
desconto e total em um dicionário. Esperado: 3 serviços de R$ 0,10 totalizam exatamente
R$ 0,30. Teste desconto zero, igual ao subtotal e maior que ele.

## C · monte uma proposta

Objetivo: associar cliente existente e serviços. Conceitos: busca por ID e cópia.
Tarefa: crie dois orçamentos para o mesmo cliente, mantendo IDs diferentes.
Esperado: ID de cliente inexistente não cria proposta. Teste que a lista original
não muda quando uma validação falha no meio da operação.

## D · texto antes do arquivo

Objetivo: apresentar dados claramente. Conceitos: f-strings e `join`. Tarefa: monte
uma lista de linhas com título, cliente, itens e total. Esperado: preço R$ 12,50 e
total R$ 25,00 para duas unidades. Verifique o conteúdo da string em um teste antes
de tentar abrir um TXT no editor.

## E · persistência e recuperação

Objetivo: consultar propostas antigas após reiniciar. Conceitos: JSON e conversão
de tipos. Tarefa: transforme preços em strings no arquivo e use Decimal na leitura
dos cálculos. Esperado: texto do orçamento antes e depois da recuperação é igual.
Teste também um orçamento que referencia um cliente inexistente no arquivo.

No menu, se a exportação TXT falhar depois de salvar JSON, informe as duas situações
separadamente. Não diga que o orçamento inteiro desapareceu. Passe para
[depuração](04-evoluindo-o-projeto.md).
