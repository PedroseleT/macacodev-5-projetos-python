# 04 · Fila Justa 🎟️

**Intermediário · organize senhas, chamadas e atendimentos concluídos.**

Um pequeno balcão precisa saber quem aguarda, quem foi chamado e quem já terminou.
O aplicativo gera senhas comuns/prioritárias, lista filas, chama a próxima,
registra conclusão e consulta histórico/contagens após reiniciar.

## Política didática, sem certificação legal

Quando ambas as categorias aguardam, chamamos **até duas prioritárias e depois uma
comum**. Dentro de cada categoria, respeitamos FIFO: a primeira chegada sai primeiro.
Se apenas uma categoria aguarda, ela continua sendo atendida. A contagem de
prioritárias consecutivas fica limitada a dois e volta a zero após uma comum.
Se uma comum chegar depois de duas prioritárias, terá o próximo turno.

Há um único atendimento ativo. É preciso concluí-lo antes da próxima chamada.
Não há cancelamento automático, avaliação de elegibilidade ou múltiplos guichês.
Esta política serve para estudar algoritmos; não é uma implementação completa
das exigências legais de atendimento prioritário.

```text
Geradas nesta ordem: C0001, P0002, P0003, C0004, P0005
Chamadas: P0002, P0003, C0001, P0005, C0004
```

O número é global e nunca reinicia entre categorias. `P`/`C` indica categoria;
não confunda o número da senha com sua posição atual na fila.

## Executar e testar

Python 3.11+, sem dependências. Na raiz:

```sh
python 04-fila-justa/codigo-inicial/main.py
python 04-fila-justa/solucao/main.py
python 04-fila-justa/solucao/main.py --dados 04-fila-justa/dados/experimento.json
```

Menu: 1 comum, 2 prioritária, 3 fila, 4 chamar, 5 concluir, 6 histórico,
7 estatísticas e 0 sair. Histórico mostra atendimentos concluídos e informa a
chamada ativa, se existir. Estatísticas separam concluídos de aguardando/ativo.

```sh
cd 04-fila-justa
python -m unittest discover -s testes -v
```

Testes verificam FIFO, intercalação, fila vazia, categoria única, chegada de comum
após duas prioritárias, duplicatas, histórico e recuperação no meio de atendimento.

## Conceitos e estrutura

Listas como filas, condicionais, estados, cópias, funções, regras de negócio e JSON.
Pré-requisitos: listas, funções e persistência; não é necessário conhecer classes.

```text
codigo-inicial/main.py, tarefas.py
solucao/main.py
solucao/filajusta/dominio.py      política, transições e validação
solucao/filajusta/arquivos.py     arquivos UTF-8
solucao/filajusta/terminal.py     interface
testes/test_filajusta.py
passo-a-passo/                   cinco tutoriais
```

## Dados e recuperação

Padrão: `04-fila-justa/dados/fila.json`, independente do diretório atual. O arquivo
nasce na primeira alteração. Salva filas, próximo número, histórico, turno de
prioridade e atendimento ativo. Datas usam ISO com fuso UTC. Não pedimos nomes de
pessoas: a senha numérica basta para o exercício.

Ausência do arquivo inicia fila vazia. JSON inválido, senha duplicada ou contador
incompatível impede abertura sem apagar o original. Feche o programa, copie o JSON
e restaure backup/corrija o problema. Para zerar intencionalmente, mova o arquivo;
isso reinicia numeração e histórico, portanto não faça durante uso real.

Gravação por temporário preserva o destino se falhar; a interface só confirma
após salvar. Apenas uma instância por arquivo. A solução com listas é adequada a
filas pequenas para estudo, não a milhares de atendimentos simultâneos.

## Trilha

1. [Entenda](passo-a-passo/01-entenda-o-problema.md)
2. [Planeje](passo-a-passo/02-planeje-a-solucao.md)
3. [Construa](passo-a-passo/03-primeira-implementacao.md)
4. [Depure](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Evolua](passo-a-passo/05-finalizacao.md)

[Desafios](desafios.md) · [Dicas](dicas.md) · [Checklist](checklist.md) · [Voltar](../README.md)
