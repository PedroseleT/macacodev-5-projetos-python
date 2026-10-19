# Dicas progressivas

<details><summary>1 · Atualizar por onde?</summary>
Primeiro localize um ID. Faça uma cópia do estado e mude uma chave permitida.
Só depois valide e salve. Não monte um registro novo com apenas os campos recebidos.
</details>
<details><summary>2 · Como pesquisar sem mudar a lista?</summary>
Percorra todos os registros e acrescente os que combinam a uma lista nova.
Normalize o termo e o nome para comparar sem diferença de maiúsculas.
</details>
<details><summary>3 · Por que o CSV precisa de biblioteca?</summary>
Um nome com vírgula parece duas colunas quando você concatena texto. DictWriter
trata aspas e delimitadores; DictReader ajuda a testar a recuperação das colunas.
</details>
<details><summary>Meu JSON antigo não tem o campo novo</summary>
Defina um valor padrão deliberado e teste uma cópia antiga. Não apague dados para
fazer a nova função funcionar. Evoluir formato exige considerar o que já foi salvo.
</details>
