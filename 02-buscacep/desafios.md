# Ideias para continuar

Primeiro deixe a consulta básica funcionando. Depois escolha uma melhoria que
você gostaria de usar.

## Para começar: abrir um endereço do histórico

Mostre os registros com números e permita escolher um para ver todos os campos.
A ideia é reutilizar informações já salvas.

**Está pronto quando:** funciona sem uma nova consulta e avisa quando o número
escolhido não existe, inclusive se o histórico estiver vazio.

<details><summary>Uma pista</summary>
Liste os registros com <code>enumerate</code>. Confira o número antes de acessar a lista.
Mostre também quando aquela consulta foi feita.
</details>

## Um passo além: salvar um endereço em texto

Escolha uma consulta e gere um arquivo com rua, bairro, cidade e estado.
Não altere o histórico para fazer isso.

**Está pronto quando:** o arquivo abre com os acentos corretos e cada informação
tem um rótulo fácil de entender.

<details><summary>Uma pista</summary>
Monte o texto primeiro e mostre na tela. Só depois grave em um arquivo,
usando UTF-8 para preservar os acentos.
</details>

## Um desafio maior: evitar repetir uma consulta recente

Se aquele CEP foi consultado há pouco, ofereça o resultado salvo.
Deixe claro que veio do histórico e permita pedir uma atualização.

**Está pronto quando:** existe um prazo definido, resultados antigos provocam
nova consulta e uma falha de rede não aparece como endereço atualizado.

<details><summary>Uma pista</summary>
Compare a data da consulta com a hora atual antes de decidir usar a internet.
Separe a decisão de usar o histórico da função que pede o endereço.
</details>

[Voltar à última etapa](passo-a-passo/05-finalizacao.md)
