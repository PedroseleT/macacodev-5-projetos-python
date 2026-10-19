# 4. Nem toda falha é culpa do seu código

Trabalhar com internet traz uma novidade: às vezes seu programa está certo,
mas o serviço não responde. Precisamos aprender a distinguir essas situações.

## O CEP não existe

Você pode digitar oito números e ainda assim não encontrar um endereço.
O ViaCEP pode responder com `{"erro": true}`. Nesse caso, mostre “CEP não
encontrado” e deixe a pessoa tentar outro. Não acrescente isso ao histórico.

## A conexão não funcionou

Uma mensagem com `URLError` pode indicar problema na rede. Um tempo de espera
esgotado indica que não houve resposta a tempo. Mostre algo como “Não foi possível
consultar agora. Tente novamente mais tarde”.

O programa não deve ficar fazendo pedidos sem parar. Espere uma nova escolha
da pessoa no menu.

## Apareceu KeyError

Essa mensagem costuma significar que você tentou acessar uma informação que
não está no dicionário. Confira se escreveu `localidade`, e não `cidade`,
ao ler a resposta do ViaCEP.

Para investigar, mostre `print(endereco)` usando o exemplo público do tutorial.
Veja quais nomes realmente chegaram. Não precisa adivinhar.

## A resposta não era JSON

Se aparecer `JSONDecodeError`, o texto recebido não pôde ser lido como JSON.
Não transforme qualquer resposta em endereço só para o programa continuar.
Avise que o serviço enviou uma resposta inesperada.

Leia a última linha do erro, descubra a parte envolvida e corrija uma coisa
por vez. E lembre: uma consulta que falhou não deve apagar as anteriores.

[Anterior: construir](03-primeira-implementacao.md) · [Próximo: melhorar sua versão](05-finalizacao.md)
