# 01 · Desperdício Zero 🍌

**Iniciante · um pequeno inventário para lembrar a validade dos alimentos.**

Quem compra uma fruta e esquece na gaveta perde dinheiro e comida. Vamos registrar
nome, quantidade e validade, para consultar o que precisa de atenção primeiro.
Datas são um auxílio de organização, não uma avaliação de segurança alimentar.

## Demonstração

```text
1 Cadastrar | 2 Listar | 3 Próximos | 4 Vencidos | 5 Remover | 0 Sair
Escolha: 1
Alimento: Banana
Quantidade: 6
Validade (DD/MM/AAAA): 20/10/2026
Alteração salva.
Escolha: 2
1 | Banana | 6 | 2026-10-20 | proximo
```

O status depende do dia da execução: `proximo` inclui hoje e os próximos três dias;
`vencido` significa antes de hoje. São regras de data, não orientação de consumo.

## Funcionalidades e conceitos

Cadastro, listagem, próximos do vencimento, vencidos, remoção por ID e recuperação
automática em JSON. Quantidades positivas de até um bilhão, inclusive fracionárias
com vírgula ou ponto; nomes de até 120 caracteres. Datas reais em DD/MM/AAAA.
O menu trata opções inválidas, IDs ausentes e falhas de gravação.

Você pratica variáveis, tipos, operadores, `if`, `while`, `for`, funções, listas,
dicionários, `datetime`, arquivos e JSON. Precisa reconhecer funções e listas;
o tutorial apresenta as ferramentas de datas e persistência.

## Instalar e executar

Python 3.11+, sem instalação de dependências. A partir da raiz:

```sh
python 01-desperdicio-zero/codigo-inicial/main.py
python 01-desperdicio-zero/solucao/main.py
python 01-desperdicio-zero/solucao/main.py --dados 01-desperdicio-zero/dados/experimento.json
```

`codigo-inicial` abre um menu com orientações; implemente as ações progressivamente.
O esqueleto não importa a solução nem finge salvar registros.

## Arquivos e dados

```text
codigo-inicial/main.py, tarefas.py
solucao/main.py
solucao/desperdicio/dominio.py     regras e validação
solucao/desperdicio/arquivos.py    leitura e escrita UTF-8
solucao/desperdicio/terminal.py    menu e mensagens
testes/test_desperdicio.py
passo-a-passo/                    cinco etapas
```

Sem `--dados`, os registros ficam em `01-desperdicio-zero/dados/alimentos.json`,
independentemente do diretório de onde você executa o programa. Essa pasta é criada
no primeiro salvamento. Antes disso, um arquivo ausente significa inventário vazio.
O JSON contém versão, próximo ID e a lista de alimentos. IDs removidos não se repetem.

Carregamento valida estrutura, IDs, datas e quantidades. Se o arquivo estiver inválido,
o programa encerra com código 1, preservando-o. Faça uma cópia, corrija com um editor
ou restaure seu backup. Para zerar intencionalmente, feche o programa e mova/apague
somente esse JSON. Nunca faça isso como primeira tentativa de resolver um erro.

Cada alteração é escrita em temporário e substitui o destino após sucesso. Falha
de gravação não confirma a mudança em memória. Não há suporte a gravação simultânea
por várias instâncias. Faça backups por cópia com o programa fechado.

## Testes

```sh
cd 01-desperdicio-zero
python -m unittest discover -s testes -v
```

Usam datas fixas e arquivos temporários; não modificam seu inventário. Cobrem limites
de validade, ano bissexto, entradas inválidas, remoção, persistência e falha de escrita.
Para testar sua tentativa, escreva casos semelhantes importando seu módulo; a suíte
atual importa `solucao/desperdicio`.

## Trilha e próximos passos

1. [Entenda o problema](passo-a-passo/01-entenda-o-problema.md)
2. [Planeje a solução](passo-a-passo/02-planeje-a-solucao.md)
3. [Construa por etapas](passo-a-passo/03-primeira-implementacao.md)
4. [Aprenda com os erros](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Evolua sozinho](passo-a-passo/05-finalizacao.md)

[Desafios](desafios.md) · [Dicas progressivas](dicas.md) · [Checklist](checklist.md) · [Voltar](../README.md)
