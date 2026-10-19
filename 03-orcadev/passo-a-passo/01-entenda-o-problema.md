# 1. Entenda o problema

Uma pessoa pede duas revisões de página e uma configuração de formulário. Você
anota preços em mensagens diferentes, esquece um item e aplica desconto no total
errado. Um orçamento reúne escopo, quantidades e valores de forma verificável.

O programa não decide seu preço de mercado. Ele organiza os valores que você
informar e apresenta a conta. Também não é um sistema fiscal: não emite nota,
não calcula tributos e não garante validade contratual.

## Faça a conta antes de programar

Escreva dois serviços: 2 unidades a R$ 12,50 e 1 unidade a R$ 5,00. O subtotal é
R$ 30,00. Com desconto fixo de R$ 4,00, o total é R$ 26,00. O que deveria acontecer
se o desconto fosse R$ 40,00? Nesta versão, a operação é rejeitada; total negativo
não é uma proposta válida.

O resultado terá cadastro de cliente, montagem de serviços, desconto, consulta de
propostas anteriores e TXT formatado. Cada proposta tem ID próprio, inclusive
quando o mesmo cliente pede duas propostas no mesmo dia.

Você já conhece funções e JSON. Agora precisa entender **regra de negócio**: uma
decisão do problema, como desconto não superar subtotal, que deve valer tanto no
terminal quanto num teste automatizado. Se essa regra estiver só em `input`, uma
chamada direta à função poderá produzir um orçamento inválido.

Sua tarefa: descreva um orçamento válido, um sem cliente e um com quantidade
negativa. Defina a mensagem esperada antes de escrever a primeira função. Depois
vá para [modelar os dados](02-planeje-a-solucao.md).
