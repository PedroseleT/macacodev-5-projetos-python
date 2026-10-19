# Uma ajuda para encontrar o próximo passo

Você não precisa resolver o projeto inteiro de uma vez. Escolha uma dúvida.

<details><summary>Como editar sem apagar os outros campos?</summary>

**Primeira pista:** comece pela ficha existente, não por uma ficha vazia.

**Mais uma:** encontre o ID, faça uma cópia e troque só os campos escolhidos.
Confira todos os valores novos antes de salvar a mudança.

</details>

<details><summary>Como pesquisar sem perder o resto da lista?</summary>

Crie uma lista nova para os resultados. Percorra as fichas e acrescente
as que combinam. Compare os dois textos em minúsculas para que “BANANA”
encontre “Banana Sistemas”.

</details>

<details><summary>Por que não basta juntar os campos com vírgulas?</summary>

O nome de uma empresa também pode ter vírgula. A tabela acabaria com uma
coluna a mais. O módulo `csv` cuida desses detalhes para você.
Comece com `csv.DictWriter`, que escreve linhas a partir de dicionários.

</details>

<details><summary>Acrescentei um campo, mas meus dados antigos não têm ele</summary>

Defina o que esse campo deve mostrar quando estiver ausente, como uma
observação vazia. Faça uma cópia dos dados antigos antes de adaptar a leitura.
Não apague seus registros só para a novidade funcionar.

</details>

[Voltar à etapa de construção](passo-a-passo/03-primeira-implementacao.md)
