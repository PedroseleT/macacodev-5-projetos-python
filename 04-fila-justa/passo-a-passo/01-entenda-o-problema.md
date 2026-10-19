# 1. Entenda o problema

Num balcão, “quem chegou primeiro?” parece suficiente até existirem categorias de
atendimento e uma pessoa já chamada. O programa precisa responder três perguntas
diferentes: quem aguarda, quem está sendo atendido e quem terminou.

Neste laboratório não guardaremos nomes. Uma senha com número único identifica
o atendimento. A pessoa recebe uma comum ou prioritária; o sistema não avalia quem
tem esse direito. Essa decisão está fora do escopo educacional.

## Uma regra antes de uma lista

Se sempre chamarmos prioritárias enquanto existirem, comuns podem esperar
indefinidamente. Se ignorarmos a categoria, não haverá preferência. Nossa política
didática intercala até duas prioritárias e uma comum, preservando a chegada dentro
de cada categoria. Não a apresente como garantia de cumprimento de legislação.

Escreva num papel: comum 1, prioritária 2, prioritária 3, comum 4, prioritária 5.
Simule P2, P3, C1, P5, C4. Antes de cada próxima chamada, marque a anterior como
concluída. Agora simule somente prioritárias: o balcão não deve parar esperando
uma comum que não existe.

## Resultado esperado

Você poderá gerar, listar, chamar, concluir e consultar histórico e contagens.
Ao reiniciar, a senha ativa continuará ativa; não será atendida duas vezes.
A contagem da política também precisa sobreviver à reinicialização.

Sua tarefa inicial: descreva os estados e o que não pode acontecer, como chamar
com fila vazia ou concluir sem atendimento. Isso cria regras testáveis. Depois
vá para [representar os estados](02-planeje-a-solucao.md).
