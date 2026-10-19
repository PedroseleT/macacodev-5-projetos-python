# Ideias para deixar o projeto com a sua cara

Escolha uma ideia depois de terminar o básico. Não é uma lista de obrigações.

## Para começar: procurar pelo nome

Faça uma busca que encontre Banana quando a pessoa digitar “ban” ou “BAN”.
A ideia é praticar comparação de textos.

**Está pronto quando:** a busca mostra só os alimentos que combinam, avisa quando
não encontra nada e não apaga o restante da lista.

<details><summary>Uma pista</summary>
Compare os textos do mesmo jeito, por exemplo ambos em minúsculas.
Se precisar de outra direção, use <code>in</code> para procurar um trecho dentro de outro.
</details>

## Um passo além: editar um alimento

Permita corrigir nome, quantidade ou validade sem cadastrar tudo de novo.
Escolha pelo ID e mantenha esse número.

**Está pronto quando:** você consegue corrigir uma quantidade e, se a nova
validade não existir, as informações anteriores continuam guardadas.

<details><summary>Uma pista</summary>
Encontre a ficha primeiro. Confira os novos valores antes de trocar os antigos.
Reutilize as conferências que já fez no cadastro.
</details>

## Um desafio maior: mostrar o que vence primeiro

Organize a apresentação pela validade e deixe a pessoa escolher quantos dias
contam como “perto de vencer”. Não aceite um prazo negativo.

**Está pronto quando:** a lista segue a ordem das datas e mudar o prazo altera
os alertas sem mudar as validades cadastradas.

<details><summary>Uma pista</summary>
Comece organizando só três alimentos no papel. Depois conheça <code>sorted</code>.
Para validades iguais, mantenha uma ordem clara usando o ID.
</details>

[Voltar à última etapa](passo-a-passo/05-finalizacao.md)
