# 4. Aprenda com os erros

## O filtro apagou o resto das vagas

Você provavelmente atribuiu o resultado ao estado principal. Um filtro é uma
consulta, não uma exclusão. Imprima os IDs antes e depois e verifique se a função
devolve outra lista. Acrescente um teste que compara o estado original após buscar.

## Editar o cargo apagou o link

Reconstruir o registro só com os campos recebidos perde informações. Atualização
parcial deve partir do registro existente e alterar apenas chaves permitidas.
Teste preservação de empresa, link e criação ao mudar o cargo.

## A lista está vazia, mas a estatística mostra erro

Se você calcula percentuais sem verificar o total, pode dividir por zero. Nesta
versão as estatísticas são contagens; a soma de todas as categorias deve ser o total.
Teste o estado vazio antes de acrescentar qualquer fórmula.

## O CSV abriu em colunas estranhas

Pode haver separador diferente no aplicativo de planilhas, mas também pode ser
um erro seu: concatenar vírgulas sem escape. Abra com `csv.DictReader`, confira
as chaves e um nome que contenha vírgula e aspas. No Excel, escolha importar UTF-8
com delimitador vírgula em vez de alterar seu JSON para “consertar” a visualização.

## “ValueError: Invalid IPv6 URL” ao ler um link

Até a análise sintática de uma URL pode lançar exceção quando o texto é malformado.
Isole a validação de link e converta esse erro em uma mensagem do domínio. Não abra
um endereço arbitrário para descobrir se está bem formado.

## Minha exclusão removeu a candidatura errada

Verifique se você confundiu ID com posição. Uma lista filtrada tem posições
diferentes da coleção original. Localize pelo ID estável e use confirmação. Faça
um teste com dois registros da mesma empresa antes de [finalizar](05-finalizacao.md).
