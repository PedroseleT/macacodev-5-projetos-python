# 1. Entenda o problema

Imagine que você comprou bananas, arroz e iogurte. Guardou cada coisa em um lugar
e não lembra o que vence primeiro. O objetivo não é decidir se um alimento está
próprio para consumo: é deixar as datas registradas para você se organizar.

Antes de escrever código, escolha três alimentos inventados. Para cada um, anote
nome, quantidade e validade. Uma lista de nomes resolve o problema? Não: você não
saberia quanto tem nem quando vence. Por isso cada registro terá vários campos.

O usuário precisará cadastrar, consultar e remover. O programa também separará
vencidos de próximos do vencimento e recuperará os registros ao abrir novamente.
“Salvar” é parte do comportamento: uma lista que desaparece ao sair não resolve
o esquecimento de amanhã.

## Defina o que significa próximo

Escolher uma regra é trabalho de programação. Aqui, próximo significa de zero a
três dias a partir de hoje, inclusive. Ontem é vencido; hoje é próximo; daqui a
quatro dias está em dia. A regra é didática e pode virar um desafio configurável.

Desenhe a linha do tempo para o dia 18/10/2026: 17 deve ser vencido; 18 e 21,
próximos; 22, em dia. Esse desenho já é um plano de teste, antes de existir código.

## Sua primeira tarefa

Descreva uma conversa de terminal em que alguém cadastra dois produtos, lista e
remove apenas um. Inclua o que deveria acontecer com quantidade zero e com
31/02/2026. Não aceite “o programa quebra” como resposta: defina uma mensagem e
permita tentar de novo.

Você precisará de strings, números, condicionais, laços e funções. Se listas e
dicionários ainda confundirem, represente no papel uma lista com dois registros.
Explique a diferença entre o produto e a coleção inteira. Só então siga para
[o planejamento](02-planeje-a-solucao.md).
