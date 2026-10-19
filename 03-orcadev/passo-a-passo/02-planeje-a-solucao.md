# 2. Separe cliente, serviços e conta

Um orçamento junta informações diferentes. Vamos separá-las para não virar uma
lista de textos que ninguém entende depois.

Um cliente precisa de nome e número próprio. Cada serviço precisa de descrição,
quantidade e preço por unidade. O orçamento reúne os serviços de um cliente e
o desconto escolhido.

## Dinheiro merece um cuidado

Python tem uma ferramenta chamada `Decimal`, que ajuda a trabalhar com valores
decimais sem as pequenas aproximações que podem aparecer com `float`.

Veja um exemplo:

```python
from decimal import Decimal

preco = Decimal("0.10")
print(preco * 3)
```

O resultado é `0.30`. Repare nas aspas em `"0.10"`: o valor começa como texto.
Use esse cuidado também nos preços que vierem do teclado.

Vamos aceitar até duas casas depois da vírgula ou do ponto. Não precisamos
trabalhar com frações menores que um centavo neste projeto.

## Uma função para cada parte

Planeje uma função para criar o serviço, outra para somar os valores e outra
para montar o texto do orçamento. O menu pergunta e mostra; as funções fazem
as contas. Assim você consegue entender cada parte separadamente.

Na hora de salvar em JSON, o preço será texto, como `"12.50"`. Na hora de
calcular, transforme novamente em `Decimal`: JSON não guarda esse tipo diretamente.

Anote a ordem: escolher cliente, acrescentar serviços, calcular, salvar e mostrar.
Antes de seguir, confira se consegue contar esse caminho sem olhar o código.

[Anterior: a ideia](01-entenda-o-problema.md) · [Próximo: montar o orçamento](03-primeira-implementacao.md)
