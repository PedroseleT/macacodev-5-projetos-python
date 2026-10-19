# 2. Uma consulta, quatro pequenas tarefas

Vamos pensar no caminho de um CEP desde o teclado até aparecer na tela.
Não precisamos resolver tudo na mesma função.

## 1. Conferir o que foi digitado

Vamos aceitar `01001000` e `01001-000`. Os dois representam o mesmo CEP.
Depois de conferir o formato, guardaremos apenas os oito números como texto.

Por que texto? Porque `01001000` começa com zero. Transformar isso em um número
inteiro faria esse zero desaparecer. CEP é uma identificação, não uma quantidade
para somar.

## 2. Pedir o endereço

A URL do pedido terá este formato:

`https://viacep.com.br/ws/01001000/json/`

Só o trecho do CEP muda. O programa montará esse endereço a partir do CEP
conferido, sem pedir que a pessoa digite uma URL inteira.

## 3. Ler e mostrar a resposta

O serviço usa `localidade` para a cidade e `uf` para o estado.
Nosso programa deve mostrar rótulos mais amigáveis, como “Cidade: São Paulo”.

Alguns CEPs não têm rua ou bairro preenchidos. Campo vazio não significa
automaticamente que a consulta falhou.

## 4. Guardar o que deu certo

Uma consulta válida vai para a lista do histórico. Depois, salvamos essa lista
em JSON, como aprendemos antes. Uma falha de conexão não deve virar um endereço salvo.

Anote um nome de função para cada tarefa. Isso ajuda a saber onde procurar
quando uma parte não funcionar.

[Anterior: a ideia](01-entenda-o-problema.md) · [Próximo: fazer a primeira consulta](03-primeira-implementacao.md)
