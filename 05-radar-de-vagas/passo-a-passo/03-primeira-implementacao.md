# 3. Junte as peças, uma de cada vez

Abra `codigo-inicial/main.py` para conhecer o menu e `codigo-inicial/tarefas.py`
para começar suas funções. Rode a partir da pasta principal da trilha:

```sh
python 05-radar-de-vagas/codigo-inicial/main.py
```

O menu mostra as tarefas previstas, não um gerenciador pronto. Vamos dar vida
às opções aos poucos.

## Cadastre e mostre

Crie uma ficha com empresa, cargo, link, data e status. Confira se os campos
obrigatórios estão preenchidos. Use um endereço de exemplo, como
`https://example.org/vaga`. Verificar o formato do link não exige abrir o site.

Cadastre duas vagas da mesma empresa e mostre os IDs diferentes na listagem.

## Acrescente pesquisa e filtro

Pesquise por parte do nome, sem diferenciar maiúsculas de minúsculas.
Depois faça o filtro por status. Crie uma nova lista para o resultado:
a lista completa precisa continuar guardada.

## Altere e exclua com cuidado

Use o ID para escolher a vaga. Ao editar o cargo, mantenha os outros campos.
Ao mudar de Interesse para uma etapa de candidatura, peça a data se faltar.

Antes de excluir, mostre qual registro será removido e peça confirmação.
Se a pessoa cancelar, nada deve mudar.

## Guarde e conte

Salve em JSON após mudanças e carregue ao abrir. Para as estatísticas, comece
contando quantas fichas estão em cada status.

Por último, use o módulo `csv` para exportar uma tabela. Ele lida com nomes
que tenham vírgulas e aspas. Abra a tabela e compare com a listagem antes
de considerar essa parte pronta.

[Anterior: organizar](02-planeje-a-solucao.md) · [Próximo: resolver os tropeços](04-evoluindo-o-projeto.md)
