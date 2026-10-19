# 4. Minha conta ficou estranha. E agora?

Com dinheiro, uma tela bonita não resolve se a conta estiver errada. Vamos olhar
algumas situações que podem aparecer enquanto você constrói.

## O número tem casas demais

Confira de onde veio o preço. Se você usou `float` antes de criar o `Decimal`,
a aproximação já aconteceu. Prefira transformar o texto diretamente:
`Decimal("12.50")`.

Para investigar, use `print(type(preco), preco)`. O primeiro valor mostra
o tipo da informação; o segundo mostra o conteúdo. Retire essa mensagem quando
entender o problema.

## Não consegui salvar Decimal no JSON

Pode aparecer uma mensagem dizendo que `Decimal` não pode ser convertido para
JSON. Não precisa abandonar a ferramenta: salve o preço como texto e transforme
em `Decimal` novamente quando precisar calcular.

Pense nisso como mudar a embalagem para guardar, sem mudar o valor.

## O total ficou negativo

Confira se o desconto é menor ou igual ao subtotal. Essa conferência deve estar
na função que calcula, não apenas na pergunta do menu. Dessa forma a regra
continua valendo quando você reutilizar a função em outra parte.

## O arquivo de texto não apareceu

Salvar os dados do orçamento e criar o texto são tarefas diferentes.
Se o cadastro foi salvo, não cadastre tudo novamente. Na solução pronta,
a opção de exportar permite gerar de novo o texto de um orçamento existente.

Leia a mensagem com calma e identifique qual parte falhou antes de mexer.
Um problema no arquivo de texto não deve apagar um orçamento já guardado.

[Anterior: construir](03-primeira-implementacao.md) · [Próximo: personalizar](05-finalizacao.md)
