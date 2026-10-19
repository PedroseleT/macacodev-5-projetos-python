# 1. Quem é o próximo?

Imagine um balcão com pessoas esperando. Uma pega a senha, outra chega depois,
uma terceira precisa de atendimento prioritário. Quem deve ser chamado agora?

Vamos construir um programa para ajudar a organizar isso. Ele vai gerar senhas,
mostrar quem aguarda, chamar uma pessoa e registrar quando o atendimento terminar.

## Antes do código, uma regra clara

Neste exercício, vamos chamar até duas senhas prioritárias e depois uma comum,
quando as duas categorias tiverem pessoas esperando.

Dentro de cada categoria, quem chegou primeiro continua na frente.
Se só houver uma categoria, chamamos quem estiver nela: ninguém fica parado
esperando uma pessoa que nem chegou.

Essa é uma regra de estudo, não uma implementação completa das exigências
legais de atendimento prioritário. O programa também não decide quem tem direito
à prioridade.

## Vamos brincar de balcão no papel

Anote a chegada destas senhas: C1, P2, P3, C4 e P5.
O C significa comum; o P significa prioritária. O número identifica a senha.

Seguindo nossa regra, a chamada será P2, P3, C1, P5 e C4.
Entre uma chamada e outra, precisamos concluir o atendimento anterior.

Perceba que “estar esperando”, “estar sendo atendido” e “já ter terminado”
são situações diferentes. Nosso programa precisa lembrar das três.

Antes de seguir, faça uma rodada só com senhas comuns. A ordem ficou clara?
Esse pequeno exemplo vai ajudar bastante quando chegarmos às condições em Python.

[Voltar à apresentação](../README.md) · [Próximo: organizar a fila](02-planeje-a-solucao.md)
