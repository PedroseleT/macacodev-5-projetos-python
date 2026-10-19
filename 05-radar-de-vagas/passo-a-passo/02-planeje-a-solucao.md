# 2. Planeje a solução

Entradas: campos da vaga, ID, status, termo de pesquisa e confirmação. Saídas:
registros, contagens, JSON e CSV. Separe consulta de alteração: pesquisar não deve
salvar nem mudar o registro por acidente.

Um dicionário representa uma candidatura. Uma lista mantém as candidaturas, com
`proximo_id` fora dos registros. Acrescente `criada_em` e `atualizada_em`: são
instantes do cadastro, diferentes da data de candidatura informada pelo usuário.

## Contratos das operações

- `cadastrar`: valida campos e devolve estado com novo registro.
- `localizar`: encontra exatamente um ID ou informa que não existe.
- `atualizar`: recebe apenas campos editáveis e valida o resultado completo.
- `excluir`: remove apenas o ID escolhido, sem renumerar.
- `filtrar` e `pesquisar`: devolvem resultados sem alterar o estado.
- `estatisticas`: conta por status, inclusive zeros.

```text
carregar e validar JSON
repetir menu
    se consulta: mostrar resultado
    se alteração: construir novo estado, validar, salvar e confirmar
    se exportação: produzir CSV sem modificar JSON
```

Decida atualização parcial: campos ausentes ficam como estavam; campos enviados
vazios passam pela validação. Apagar data não pode deixar uma candidatura em
Entrevista sem data. Um erro em um campo impede a alteração inteira.

## CSV não é juntar com vírgulas

Uma empresa pode se chamar `Empresa, Demonstração`. Se você montar texto manual,
essa vírgula vira coluna extra. Use a biblioteca `csv`, que trata delimitadores e
aspas. Nomes iniciados por sinais de fórmula também exigem cuidado ao abrir numa
planilha; a exportação protege esses campos sem alterar o cadastro.

Desenhe um JSON e um CSV de dois registros. Depois siga para
[a construção incremental](03-primeira-implementacao.md).
