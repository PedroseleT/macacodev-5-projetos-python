# 3. Vamos montar o primeiro orçamento

Comece abrindo `codigo-inicial/main.py` e `codigo-inicial/tarefas.py`.
O primeiro mostra o menu. No segundo, você vai acrescentar suas funções e
substituir as orientações pelo comportamento que construir.

Na pasta principal da trilha, rode:

```sh
python 03-orcadev/codigo-inicial/main.py
```

## Um cliente, depois um serviço

Guarde um cliente em um dicionário com ID e nome. Não aceite nome em branco.
Depois, faça uma função para criar um serviço com descrição, quantidade inteira
e preço em `Decimal`.

Comece com valores escritos no código. Quando essa parte estiver clara, conecte
as perguntas do menu às funções.

## Faça a conta aparecer

Multiplique a quantidade de cada serviço pelo preço. Some os resultados.
Essa soma é o subtotal. Depois tire o desconto e mostre os três valores.

Use o exemplo da página anterior: subtotal de R$ 30,00 e desconto de R$ 4,00
precisam chegar a R$ 26,00. Se o desconto passar do subtotal, peça outro valor.

## Organize a apresentação

Monte um texto com título, nome do cliente, serviços e total. Uma lista de linhas
pode ajudar; `"\n".join(linhas)` junta essas linhas com uma quebra entre elas.

Só depois salve esse texto em um arquivo `.txt`. Guarde também os dados do
orçamento em JSON, para consultar e gerar o texto de novo sem refazer o cadastro.

Crie outro orçamento para o mesmo cliente. Os dois precisam ter números próprios
e continuar disponíveis depois que o programa for fechado.

[Anterior: organizar](02-planeje-a-solucao.md) · [Próximo: conferir o que deu errado](04-evoluindo-o-projeto.md)
