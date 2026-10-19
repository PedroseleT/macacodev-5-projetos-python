# 1. Entenda o problema

Você encontra uma vaga, salva o link numa mensagem e envia currículo para outra.
Uma semana depois não lembra se já se candidatou nem quando veio o retorno.
O Radar será um registro seu, não um robô que encontra ou se candidata a vagas.

Cada oportunidade reúne empresa, cargo, link, data e status. O mesmo nome de empresa
pode aparecer em vagas distintas: identidade será o ID da candidatura, não o nome.
Você precisa consultar e corrigir informações sem recriar tudo.

## Da oportunidade ao acompanhamento

Interesse significa que você ainda pode estar avaliando a vaga; a data de envio
pode estar vazia. Ao marcar Candidatura enviada, Entrevista ou outra etapa,
informe a data da candidatura. Estados são anotações manuais, não evidência de
aprovação obtida automaticamente.

O resultado final terá cadastro, listagem, busca, filtro, edição, exclusão,
estatísticas, JSON e CSV. CSV permite abrir uma tabela em outra ferramenta; JSON
continua sendo a fonte usada pelo programa ao reiniciar.

## Antes de escrever código

Crie três oportunidades genéricas no papel: duas na mesma empresa, uma em Interesse
e outra em Entrevista. Pergunte: buscar pelo nome deve retornar uma ou ambas?
Excluir uma deve excluir a outra? Uma pergunta define o filtro; a outra mostra
por que precisamos de ID estável.

Você já praticou cadastro, regras e persistência. Agora vai combinar essas decisões
sem colocar tudo no menu. Explique CRUD em palavras próprias e siga para
[planejar o modelo](02-planeje-a-solucao.md).
