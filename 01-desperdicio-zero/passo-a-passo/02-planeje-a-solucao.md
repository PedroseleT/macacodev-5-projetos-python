# 2. Vamos organizar as ideias

Antes de programar, vamos dividir a ideia em pedaços que cabem na cabeça.
“Fazer um gerenciador de alimentos” parece grande. “Guardar o nome de uma banana”
já parece um começo possível, né?

## Um alimento e uma lista de alimentos

Um alimento tem informações que ficam juntas. Em Python, um dicionário pode
guardar essas informações usando nomes para cada uma:

```python
alimento = {"nome": "Banana", "quantidade": 6}
print(alimento["nome"])
```

A saída será `Banana`. O texto `"nome"` funciona como a etiqueta de uma gaveta:
você usa a etiqueta para encontrar o valor. Acrescentaremos a validade depois.

Para guardar vários alimentos, usaremos uma lista de dicionários. Não precisa
decorar essa frase: pense em uma caixa com várias fichas dentro.

## Nosso caminho

1. Criar uma ficha de alimento.
2. Colocar mais de uma ficha na lista.
3. Mostrar as fichas na tela.
4. Acrescentar a validade e comparar com o dia de hoje.
5. Remover um alimento.
6. Salvar a lista para abrir de novo depois.

Cada alimento também terá um número próprio, chamado ID. Ele ajuda a escolher
qual remover, inclusive quando dois alimentos têm o mesmo nome.

Uma função será uma pequena tarefa com nome, como `cadastrar` ou `listar`.
Não coloque tudo dentro de uma função gigante.

Anote quais informações entram e o que você espera ver na tela. Comece com dois
alimentos: é mais fácil acompanhar uma lista pequena antes de pensar em cinquenta.

[Anterior: a ideia](01-entenda-o-problema.md) · [Próximo: começar o programa](03-primeira-implementacao.md)
