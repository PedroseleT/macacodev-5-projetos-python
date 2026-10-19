# 1. Um CEP pode poupar bastante digitação

Você começa a preencher um endereço: rua, bairro, cidade, estado... Não seria
melhor informar só o CEP e deixar o programa procurar parte dessas informações?

É isso que vamos construir. Diferente do primeiro projeto, agora nem tudo virá
do teclado. Nosso programa vai pedir ajuda a outro serviço pela internet.

## Sem mistério com os nomes

Uma **API** é uma forma de um programa pedir informações a outro. Pense num
balcão: você faz um pedido seguindo algumas regras e recebe uma resposta.

Aqui, usaremos o ViaCEP, um serviço público de consulta de endereços. Você envia
um CEP e recebe informações como cidade e estado. Não precisa criar conta nem
conseguir uma chave para usar este projeto.

O pedido pela internet é chamado de **requisição HTTP**. A resposta vem em
**JSON**, aquele texto organizado que apareceu no projeto anterior. Vamos ver
um exemplo pequeno antes de juntar tudo.

## O que o programa fará?

Ele pedirá o CEP, mostrará o endereço e guardará as consultas que deram certo.
Você também poderá consultar o histórico sem fazer outro pedido pela internet.

Mas a internet pode falhar. Um CEP também pode ter o formato certo e não existir.
Precisamos explicar essas situações sem fechar o programa do nada.

Antes de seguir, escreva como seria uma consulta bem-sucedida e como você
gostaria de ser avisado se não houvesse conexão. Não precisa escrever código ainda.

[Voltar à apresentação](../README.md) · [Próximo: dividir a consulta em partes](02-planeje-a-solucao.md)
