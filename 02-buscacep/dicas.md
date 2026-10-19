# Uma ajuda para a consulta

Não precisa ler tudo. Abra a dúvida que apareceu na sua tentativa.

<details><summary>Por que o zero do começo desapareceu?</summary>

**Primeira pista:** CEP não é uma quantidade para fazer contas.

**Mais uma:** deixe como texto. Transformar em inteiro tira o zero inicial.
Você pode conferir os dígitos sem mudar o CEP para número.

</details>

<details><summary>Não entendi como ler a resposta</summary>

**Primeira pista:** veja o exemplo pequeno com `json.loads` na etapa de construção.

**Mais uma:** depois da conversão, você terá um dicionário.
`endereco["localidade"]` busca a cidade. Confira os nomes dos campos
na resposta antes de escrever o acesso.

</details>

<details><summary>Rua vazia quer dizer que deu errado?</summary>

Nem sempre. Há CEPs de uma cidade que não apontam para uma rua específica.
Uma resposta com cidade e estado pode ser válida mesmo sem rua ou bairro.
Já `{"erro": true}` significa que o CEP não foi encontrado.

</details>

<details><summary>O histórico precisa de internet?</summary>

Não. O histórico lê o que você já salvou no computador.
Só uma nova consulta precisa falar com o ViaCEP. Guarde os endereços
que deram certo, não as mensagens de erro.

</details>

[Voltar à etapa de construção](passo-a-passo/03-primeira-implementacao.md)
