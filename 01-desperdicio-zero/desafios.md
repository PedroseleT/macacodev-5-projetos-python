# Desafios: primeiro tente

## Fácil · pesquisa por nome
Descrição: localizar “banana” mesmo digitando “BAN”. Objetivo: praticar strings e
filtros. Requisitos: busca parcial, sem distinguir maiúsculas; lista vazia quando
nada combinar. Concluído quando “arroz” não aparece numa busca por “ban” e a lista
original não muda. Dicas: pense em normalizar ambos os textos; depois em `casefold`.

## Médio · editar um alimento
Descrição: corrigir nome, quantidade ou validade por ID. Objetivo: reutilizar validação.
Requisitos: não trocar ID; campos vazios podem significar manter o valor, se isso
estiver documentado. Concluído quando uma validade inválida não altera nenhum campo.
Dicas: localize primeiro; construa uma cópia; salve somente depois de validar tudo.

## Avançado · painel de planejamento
Descrição: ordenar por validade e permitir prazo configurável de alerta. Objetivo:
combinar ordenação e regras. Requisitos: vencidos separados e desempate por ID;
prazo inteiro não negativo. Concluído quando testes cobrem empate, zero dias e lista
vazia. Dicas: experimente `sorted` com duas chaves antes de mexer no menu.
