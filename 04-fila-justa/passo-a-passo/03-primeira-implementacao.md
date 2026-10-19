# 3. Vamos colocar a fila para andar

Abra `codigo-inicial/main.py` para conhecer o menu e `codigo-inicial/tarefas.py`
para começar suas funções. As opções ainda mostram orientações: você vai conectar
cada uma ao que construir.

Rode pela pasta principal da trilha:

```sh
python 04-fila-justa/codigo-inicial/main.py
```

## Primeiro, gere e mostre senhas

Comece só com a fila comum. Cada nova senha precisa de um número maior que
o anterior. Use `append` para acrescentar ao fim da lista e `for` para mostrar
quem está esperando.

Depois acrescente a fila prioritária. O número não se repete entre categorias:
podemos ter C1 e P2, mas não precisamos criar duas senhas com o mesmo número.

## Faça uma chamada simples

Se só houver comuns, retire a primeira e guarde como senha em atendimento.
Em uma lista, `pop(0)` retira o primeiro elemento. Antes disso, confira se
existe alguém para chamar.

Acrescente a opção de concluir: ela leva a senha em atendimento para o histórico
e deixa o balcão livre.

## Agora coloque a regra de prioridade

Use um contador para lembrar quantas prioritárias foram chamadas seguidas.
Quando chegar a duas e houver comum esperando, chame uma comum e zere o contador.

Acompanhe o exemplo C1, P2, P3, C4, P5 no papel e no programa.

Por último, salve as listas, o atendimento, o histórico e os contadores em JSON.
Feche e abra no meio de um atendimento: a senha deve continuar ali, sem voltar
para o fim da fila.

[Anterior: organizar](02-planeje-a-solucao.md) · [Próximo: encontrar os enganos](04-evoluindo-o-projeto.md)
