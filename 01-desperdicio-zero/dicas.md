# Travou em alguma parte?

Abra só a ajuda que combina com sua dúvida. Leia uma pista e volte ao código:
não precisa entender todas de uma vez.

<details><summary>Como guardo as informações de um alimento?</summary>

**Primeira pista:** pense numa ficha com nome, quantidade e validade.

**Mais uma:** um dicionário junta esses campos; uma lista guarda várias fichas.
Comece com um alimento antes de tentar cadastrar dez.

</details>

<details><summary>Não sei como saber se está perto de vencer</summary>

**Primeira pista:** compare a validade com o dia de hoje.

**Mais uma:** transforme os dois valores em datas. Ao subtrair, use `.days`
para obter quantos dias faltam. Menos de zero já venceu; de zero a três está perto.

</details>

<details><summary>Fechei o programa e perdi a lista</summary>

**Primeira pista:** uma lista só fica na memória enquanto o programa está aberto.

**Mais uma:** o módulo `json` transforma seus dados em texto para salvar.
Carregue esse arquivo ao iniciar. Arquivo que não existe é diferente de arquivo
que existe mas está com problema: não apague o segundo automaticamente.

</details>

<details><summary>Removi o alimento errado</summary>

Use o ID mostrado na ficha, não a posição na lista. Quando um alimento sai,
a posição dos outros muda, mas o número próprio de cada um deve continuar igual.

</details>

[Voltar à etapa de construção](passo-a-passo/03-primeira-implementacao.md)
