# A conta travou? Aqui vão algumas pistas

Escolha só a parte que está tentando construir agora.

<details><summary>Por onde começo a soma?</summary>

**Primeira pista:** calcule um serviço: quantidade vezes preço.

**Mais uma:** depois faça isso para cada serviço e some os resultados.
Deixe o desconto para quando essa soma já estiver aparecendo corretamente.

</details>

<details><summary>Não entendi as aspas no Decimal</summary>

Use `Decimal("12.50")`: as aspas entregam o valor como texto, sem passar
antes pela aproximação de um `float`. A ferramenta transforma esse texto
no número que vamos usar na conta.

</details>

<details><summary>Como guardo o preço no JSON?</summary>

**Primeira pista:** JSON não precisa guardar todos os tipos que Python conhece.

**Mais uma:** salve `"12.50"` como texto e transforme em `Decimal` de novo
quando for calcular. Não transforme em `float` só para conseguir salvar.

</details>

<details><summary>Não sei como criar o arquivo do orçamento</summary>

Primeiro monte uma lista de linhas: título, cliente, serviços, subtotal,
desconto e total. Junte com `"\n".join(linhas)` e mostre na tela.
Quando gostar do resultado, grave esse texto em um arquivo.

</details>

[Voltar à etapa de construção](passo-a-passo/03-primeira-implementacao.md)
