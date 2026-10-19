# 2. Cada senha no seu lugar

Para acompanhar a fila, vamos usar duas listas: uma para senhas comuns e outra
para prioritárias. Quem chega entra no fim da sua lista. Quem é chamado sai
do começo.

Pense em duas filas desenhadas no papel. Você não precisa misturar tudo e tentar
descobrir depois quem tem preferência.

## Não basta guardar quem espera

Precisamos lembrar também de quem está sendo atendido. Essa senha já saiu da
fila, mas ainda não entrou no histórico de atendimentos concluídos.

Nossa organização terá:

- As duas listas de espera.
- A senha em atendimento, se houver uma.
- A lista de atendimentos terminados.
- O próximo número de senha.
- Quantas prioritárias já foram chamadas seguidas.

Esse último contador ajuda a saber quando chegou a vez de uma senha comum.

## Pequenas funções

Uma função gera a senha. Outra escolhe quem será chamado. Outra conclui o
atendimento. O menu só pergunta o que a pessoa quer fazer e mostra o resultado.

Ao chamar, primeiro confira se já existe alguém sendo atendido. Se existir,
peça para concluir antes de chamar outro. Se as duas filas estiverem vazias,
mostre uma mensagem em vez de tentar retirar alguém.

Na hora de salvar em JSON, guarde todas essas informações, não só as listas.
Se o programa fechar no meio de um atendimento, precisamos lembrar onde parou.

Desenhe o caminho de uma senha: espera, atendimento e histórico. Agora estamos
prontos para transformar esse desenho em código.

[Anterior: a ideia](01-entenda-o-problema.md) · [Próximo: montar o balcão](03-primeira-implementacao.md)
