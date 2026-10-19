# Desafios

## Fácil · validade da proposta
Descrição: adicionar data de validade. Objetivo: aplicar datas num novo contexto.
Requisitos: validade não anterior à emissão; mostrar no TXT. Conclusão: datas
inválidas são rejeitadas e propostas antigas continuam consultáveis. Dicas: valide
separadamente; compare objetos date; teste o limite de igualdade.

## Médio · desconto percentual
Descrição: aceitar percentual opcional em vez de desconto fixo. Objetivo: regras
monetárias. Requisitos: de 0 a 100, Decimal, modo explícito e arredondamento documentado.
Conclusão: 100% zera o total e um exemplo com fração de centavo tem resultado testado.
Dicas: calcule percentual/100; escolha ROUND_HALF_UP; nunca misture os dois modos.

## Avançado · resumo em CSV
Descrição: exportar propostas com ID, cliente, data e total. Objetivo: integração
com planilhas. Requisitos: biblioteca csv, UTF-8, campos com vírgula preservados e
nenhuma fórmula executável em nomes. Conclusão: csv.DictReader recupera as colunas
e os valores sem alterar o JSON. Dicas: gere primeiro em StringIO; faça um teste de
ida e volta; trate textos que começam com `=` antes de abrir em planilhas.
