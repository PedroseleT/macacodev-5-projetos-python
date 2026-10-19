# 1. Entenda o problema

Você já precisou preencher a cidade, o bairro e a rua repetidamente? Um CEP pode
ser usado para consultar parte desse endereço. O problema deixa de ser “guardar
tudo que o usuário digitou” e passa a incluir “pedir informação a outro sistema”.

Uma **API** é uma interface pela qual programas conversam. Pense num balcão com
regras: você faz um pedido no formato aceito e recebe uma resposta também definida.
Isso não significa que o serviço sempre estará disponível ou que aceitará qualquer
texto enviado.

Neste projeto, o pedido é uma **requisição HTTP** para uma URL do ViaCEP. A
**resposta HTTP** tem um status, como 200 quando a consulta é atendida, e um corpo.
O corpo esperado usa **JSON**, texto estruturado com chaves e valores. Python pode
transformar esse texto em um dicionário com `json.loads`.

Exemplo de pedido: `https://viacep.com.br/ws/01001000/json/`. Você solicita um CEP
específico, não uma lista de moradores. A resposta contém campos como `localidade`
e `uf`. Confira o [contrato oficial](https://viacep.com.br/) antes de programar.

## Sua tarefa antes do código

Escreva quatro conversas: CEP válido; texto com letras; CEP de oito dígitos que
não existe; conexão indisponível. Qual erro pode ser descoberto antes da internet?
Qual depende da resposta do servidor? Essa separação evita chamadas desnecessárias.

O resultado final terá um menu para consultar várias vezes e ver consultas já
salvas. Somente respostas válidas entram no histórico. Você já conhece listas,
funções e JSON; agora aprenderá a tratar uma fronteira externa. Siga para
[planejar essa fronteira](02-planeje-a-solucao.md).
