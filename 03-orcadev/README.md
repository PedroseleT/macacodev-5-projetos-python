# 03 · OrçaDev 💼

**Intermediário · transforme uma lista de serviços em um orçamento consultável.**

Freelancers precisam explicar o que será feito e quanto custará. O OrçaDev registra
clientes, serviços e quantidades; calcula subtotal, desconto fixo opcional e total;
salva múltiplas propostas em JSON e gera um documento TXT para cada uma.

```text
ORÇAMENTO 0001
Cliente: Cliente de demonstração
Data: 2026-10-18

SERVIÇOS
Revisão de página | 2 x R$ 12,50 = R$ 25,00

Subtotal: R$ 25,00
Desconto: R$ 5,00
TOTAL: R$ 20,00
```

## Regras e aprendizado

O cliente tem nome e ID; não pedimos CPF, endereço ou telefone. Cada orçamento
pertence a um cliente existente e contém de 1 a 100 serviços. Quantidade é inteira
de 1 a um milhão. Preço unitário é positivo, até um bilhão de reais e no máximo duas
casas decimais. Digite `12,50` ou `12.50`, sem separador de milhar ou símbolo R$.
Desconto é um valor fixo em reais, de zero ao subtotal; desconto percentual é desafio.

Todos os cálculos usam `Decimal`, criado de texto, nunca de `float`. Valores no
JSON são strings decimais; isso mantém precisão na recuperação. Subtotais e totais
são recalculados a partir dos serviços, evitando números derivados conflitantes.

Conceitos: modelagem, funções, listas/dicionários, aritmética decimal, validação,
regras de negócio, formatação e arquivos. Pré-requisitos: funções, persistência JSON
e tratamento de erros dos dois projetos anteriores.

## Instalar e executar

Python 3.11+, biblioteca padrão. Na raiz:

```sh
python 03-orcadev/codigo-inicial/main.py
python 03-orcadev/solucao/main.py
python 03-orcadev/solucao/main.py --dados 03-orcadev/dados/experimento.json
```

Menu: 1 cadastra cliente; 2 monta e salva um orçamento; 3 lista propostas;
4 consulta e exporta uma proposta pelo ID; 0 sai. Você pode criar vários clientes
e propostas. Não é necessário cadastrar novamente o cliente a cada orçamento.

## Estrutura e persistência

```text
codigo-inicial/main.py, tarefas.py
solucao/main.py
solucao/orcadev/dominio.py       Decimal, clientes e orçamentos
solucao/orcadev/arquivos.py      escrita por substituição
solucao/orcadev/terminal.py      cadastro, consulta e TXT
testes/test_orcadev.py
passo-a-passo/                  cinco etapas
```

Padrão: `03-orcadev/dados/orcamentos.json`. TXT em `03-orcadev/dados/orcamentos/`,
com nomes como `orcamento-0001.txt`. Com `--dados`, TXT fica na subpasta `orcamentos`
ao lado do JSON escolhido. A opção 4 regenera o TXT do orçamento salvo, substituindo
sua exportação anterior; o JSON é a fonte oficial dos dados.

Arquivo ausente inicia cadastro vazio. JSON inválido, IDs repetidos ou proposta
sem cliente válido impedem abertura e preservam o original. Feche o programa e
copie o arquivo antes de restaurar backup. Para reiniciar intencionalmente, mova
o JSON e os TXT antigos para uma pasta de backup. Pastas de dados são ignoradas
pelo Git. Não use duas instâncias gravando o mesmo arquivo.

JSON e TXT são gravações separadas: se JSON foi salvo e TXT falhou, a proposta
continua no histórico. O terminal informa isso; use opção 4 para tentar novamente.
É uma ferramenta educacional, sem nota fiscal, assinatura ou validade jurídica
garantida do documento.

## Testes

```sh
cd 03-orcadev
python -m unittest discover -s testes -v
```

Cobrem centavos, descontos, serviços inválidos, cliente inexistente, múltiplas
propostas, texto, recuperação e fluxo do menu. Nenhum dado de cliente real é usado.

## Trilha

1. [Problema](passo-a-passo/01-entenda-o-problema.md)
2. [Planejamento](passo-a-passo/02-planeje-a-solucao.md)
3. [Construção](passo-a-passo/03-primeira-implementacao.md)
4. [Erros](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Autonomia](passo-a-passo/05-finalizacao.md)

[Desafios](desafios.md) · [Dicas](dicas.md) · [Checklist](checklist.md) · [Voltar](../README.md)
