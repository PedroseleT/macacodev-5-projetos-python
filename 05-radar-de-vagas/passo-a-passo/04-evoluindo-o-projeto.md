# 4. Acompanhe o que mudou e o que deveria ficar

Neste projeto, algumas ações só mostram informações; outras mudam o que está
salvo. Confundir as duas coisas é uma fonte comum de dor de cabeça.

## Fiz uma busca e as outras vagas sumiram

Talvez você tenha colocado o resultado da pesquisa no lugar da lista completa.
Uma busca deve devolver outra lista, sem substituir o cadastro inteiro.

Mostre os IDs antes e depois da pesquisa com `print`. A lista principal deve
continuar com a mesma quantidade de vagas.

## Mudei o cargo e perdi o link

Se você criar uma ficha nova só com os campos digitados na edição, os outros
ficam de fora. Parta da ficha existente e troque apenas o que a pessoa escolheu.

Não altere o ID: ele continua identificando a mesma oportunidade.

## Excluí uma vaga, mas saiu outra

A posição de uma ficha na busca pode ser diferente da posição na lista completa.
Procure pelo ID, não pela posição que apareceu na tela.

Mostrar a empresa e o cargo antes da confirmação também ajuda a evitar enganos.

## A tabela ficou estranha na planilha

Use o módulo `csv`, em vez de juntar os campos colocando vírgulas manualmente.
Se o arquivo estiver certo, mas a planilha mostrar tudo numa coluna, procure a
opção de importar usando vírgula como separador e UTF-8 para os acentos.

Se aparecer uma mensagem de erro, leia a última linha e acompanhe a função
indicada. Resolva uma situação pequena antes de continuar acrescentando opções.

[Anterior: construir](03-primeira-implementacao.md) · [Próximo: sua próxima criação](05-finalizacao.md)
