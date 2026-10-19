# Uma ajuda para desembolar a fila

Acompanhe poucas senhas por vez. Abra a pista da parte em que travou.

<details><summary>Estou chamando a última pessoa da lista</summary>

**Primeira pista:** confira de qual lado da lista você está retirando.

**Mais uma:** `pop()` tira a última; `pop(0)` tira a primeira.
Antes de usar, confira se existe alguém esperando.

</details>

<details><summary>Como sei quando chegou a vez de uma comum?</summary>

Guarde um contador de prioritárias chamadas seguidas. Quando chegar a duas
e houver uma comum esperando, chame a comum e zere esse contador.

Se só houver prioritárias, continue atendendo. A preferência não precisa
segurar a fila quando não existe alguém da outra categoria.

</details>

<details><summary>Por que o contador precisa ser salvo?</summary>

**Primeira pista:** fechar o programa apaga as variáveis que só estavam na memória.

**Mais uma:** a próxima chamada depende do que aconteceu antes. Guarde o contador
junto das filas no JSON para não perder essa informação ao reabrir.

</details>

<details><summary>Chamar já conta como atendimento concluído?</summary>

Não. Primeiro a senha sai da espera e fica em atendimento. Só quando você
escolhe concluir ela vai para o histórico e aumenta o total de concluídos.

</details>

[Voltar à etapa de construção](passo-a-passo/03-primeira-implementacao.md)
