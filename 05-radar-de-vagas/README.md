# 05 · Radar de Vagas Dev 🚀

**Desafio final · organize sua busca de oportunidades sem perder o acompanhamento.**

O Radar registra empresas, cargos, links, data de candidatura e status. Você pode
listar, pesquisar por parte da empresa, filtrar, atualizar, excluir com confirmação,
ver contagens e exportar CSV. Os registros sobrevivem ao reinício via JSON.
O programa não busca vagas, envia candidaturas ou faz scraping: os dados são manuais.

```text
Empresa: Empresa de demonstração
Cargo: Estágio em desenvolvimento
Link completo da vaga: https://example.org/vaga
Número do status: 2
Data candidatura DD/MM/AAAA (vazio só para Interesse): 18/10/2026
Alteração salva.
1 | Empresa de demonstração | Estágio em desenvolvimento | Candidatura enviada | 2026-10-18
```

`example.org` é um domínio reservado para exemplos, não uma vaga anunciada.

## Regras, estados e conceitos

Status: Interesse, Candidatura enviada, Entrevista, Teste técnico, Proposta,
Aprovado e Rejeitado. O menu mostra os números correspondentes. Status são
acompanhamento manual, não inferências sobre o processo seletivo.

Uma oportunidade em Interesse pode ter data de candidatura vazia, pois ainda não
foi enviada. Nos outros estados, a data é obrigatória. Ao avançar do Interesse sem
data, o menu pede a data na mesma operação. Formato de entrada DD/MM/AAAA; no JSON,
AAAA-MM-DD. Datas de criação/atualização usam UTC com fuso. Não existe restrição de
sequência entre estados: você pode corrigir um status lançado errado.

Empresa e cargo têm de 1 a 160 caracteres; link deve ser HTTP/HTTPS completo, sem
credenciais nem espaços. Validar formato não verifica se a vaga continua aberta.
IDs são estáveis, não reutilizados após exclusão. Atualizar um campo não apaga os
demais; uma atualização inválida não modifica parcialmente o registro original.

Você pratica CRUD (criar, ler, atualizar e excluir), modelagem, filtros, funções,
módulos, validação, persistência, CSV, testes e refatoração. Pré-requisitos: os quatro
projetos anteriores ou capacidade de explicar suas principais decisões.

## Instalação e execução

Python 3.11+, nenhuma dependência. Na raiz:

```sh
python 05-radar-de-vagas/codigo-inicial/main.py
python 05-radar-de-vagas/solucao/main.py
python 05-radar-de-vagas/solucao/main.py --dados 05-radar-de-vagas/dados/experimento.json
```

Menu: 1 cadastrar, 2 listar, 3 filtrar status, 4 pesquisar empresa, 5 atualizar,
6 excluir, 7 estatísticas, 8 CSV, 0 sair. Para editar, informe ID e nome do campo;
para excluir, confira o registro mostrado e digite `SIM`.

## Estrutura e arquivos

```text
codigo-inicial/main.py, tarefas.py
solucao/main.py
solucao/radar/dominio.py        CRUD e validação
solucao/radar/exportacao.py     CSV com biblioteca padrão
solucao/radar/arquivos.py       JSON e escrita por substituição
solucao/radar/terminal.py       interface
testes/test_radar.py
passo-a-passo/                 cinco tutoriais
```

JSON padrão: `05-radar-de-vagas/dados/candidaturas.json`. CSV:
`05-radar-de-vagas/dados/exportacoes/candidaturas.csv`. Com `--dados`, as exportações
ficam em `exportacoes/` ao lado do JSON escolhido. Exportar substitui o CSV anterior
com o estado atual, sem modificar o JSON. Campos incluem ID, empresa, cargo, link,
data e status. Usa UTF-8 e vírgula; no Excel escolha importar CSV com essa codificação.

Nomes que começam com `=`, `+`, `-` ou `@` recebem apóstrofo somente no CSV, evitando
interpretação como fórmula em planilhas. As strings originais no JSON permanecem
iguais. Vírgulas e aspas são escapadas por `csv.DictWriter`.

Arquivo ausente inicia lista vazia. JSON inválido, versão desconhecida, IDs repetidos
ou campos inválidos impedem abertura e preservam o arquivo. Feche o programa e faça
backup antes de restaurar/corrigir. Para zerar deliberadamente, mova o JSON antigo.
A gravação usa temporário; falha não confirma alteração em memória. Uma única
instância deve escrever em cada arquivo. Dados e exportações são ignorados no Git.

## Testes

```sh
cd 05-radar-de-vagas
python -m unittest discover -s testes -v
```

Cobrem cadastro, todos os status, atualização sem efeitos parciais, exclusão, filtros,
pesquisa, contagens, links/datas inválidos, arquivos e CSV com acentos e fórmulas.
Nenhuma vaga real ou informação pessoal é necessária.

## Trilha

1. [Entenda](passo-a-passo/01-entenda-o-problema.md)
2. [Planeje](passo-a-passo/02-planeje-a-solucao.md)
3. [Construa](passo-a-passo/03-primeira-implementacao.md)
4. [Depure](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Evolua sozinho](passo-a-passo/05-finalizacao.md)

[Desafios](desafios.md) · [Dicas](dicas.md) · [Checklist](checklist.md) · [Voltar](../README.md)
