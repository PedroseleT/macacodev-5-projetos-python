# 2. Uma vaga é uma ficha, não uma pilha de textos

Vamos guardar cada oportunidade em um dicionário. Ele terá os campos da vaga
e um ID, o número usado para encontrar aquela ficha sem confundir com outra.

Uma lista reunirá todas as fichas. Pesquisar uma empresa deve mostrar as
combinações encontradas, sem apagar as outras oportunidades da lista principal.

## Separe as tarefas

Pense nestas funções:

- Cadastrar: conferir os dados e acrescentar uma ficha.
- Listar: mostrar as fichas.
- Pesquisar: procurar parte do nome de uma empresa.
- Filtrar: mostrar só um status escolhido.
- Atualizar: mudar os campos de uma ficha existente.
- Excluir: remover apenas a ficha escolhida.
- Contar: informar quantas vagas existem em cada status.

Às vezes você verá as quatro ações de cadastro, leitura, alteração
e exclusão resumidas como **CRUD**. Por enquanto, basta entender o que cada ação
faz. Não precisa decorar a sigla.

## Editar não é cadastrar de novo

Se mudar só o cargo, a empresa e o link devem continuar iguais. Comece pela
ficha existente, confira os novos valores e só então guarde a alteração.

A data de cadastro e a data de candidatura também são coisas diferentes:
uma registra quando você criou a ficha; a outra, quando enviou a candidatura.

Vamos salvar tudo em JSON para reabrir depois. O CSV será uma cópia em formato
de tabela para usar em planilhas. Ele não substitui o arquivo principal.

Desenhe uma ficha completa antes de continuar. Isso ajuda a enxergar o que
cada função precisa receber.

[Anterior: a ideia](01-entenda-o-problema.md) · [Próximo: construir por partes](03-primeira-implementacao.md)
