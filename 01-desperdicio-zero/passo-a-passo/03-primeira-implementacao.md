# 3. Construa por etapas

Abra `codigo-inicial/main.py`. O menu funciona; `tarefas.py` mostra o próximo passo.
Crie seu módulo de regras ali. Não importe `solucao/` para completar a atividade.

## Atividade A: um registro em memória

Objetivo: transformar entradas em um dicionário. Conceitos: parâmetros e `return`.
Antes de usar `input`, chame sua função com nome “Banana”, quantidade 6 e uma data.
Tarefa: rejeite nome vazio e quantidade não positiva. Esperado: uma mensagem para
zero e um registro para 6. Teste também nome só com espaços e quantidade “duas”.

## Atividade B: uma coleção

Objetivo: cadastrar mais de um registro sem perder o anterior. Conceitos: lista,
`append` e `for`. Tarefa: crie dois alimentos e liste IDs e nomes. Esperado: dois
IDs distintos. Remova o primeiro e cadastre outro: o novo ID não pode reutilizar
o removido. Teste remoção de ID inexistente sem alterar a lista.

## Atividade C: datas

Objetivo: comparar dias, não textos. Conceitos: importação e objetos de data.
Experimente isoladamente:

```python
from datetime import date

hoje = date(2026, 10, 18)
validade = date(2026, 10, 20)
print((validade - hoje).days)
```

Tarefa: use esse número para classificar ontem, hoje, +3 e +4 dias. Só depois faça
a conversão do texto com `datetime.strptime`. Esperado: 31/02 produz erro tratado,
não uma classificação. Teste fevereiro em ano bissexto.

## Atividade D: arquivos

Objetivo: recuperar os registros após sair. Conceitos: `pathlib`, JSON e exceções.
Experimente `json.dumps` em uma lista e `json.loads` no resultado, ainda sem disco.
Observe que JSON é texto, enquanto o dicionário é uma estrutura em memória.

Tarefa: grave em UTF-8 e leia ao iniciar. Esperado: cadastrar, sair e abrir mantém
o item. Arquivo ausente inicia vazio; arquivo inválido mostra erro e é preservado.
Teste em um caminho descartável, nunca no único arquivo com seus dados.

Conecte as funções ao menu uma a uma. Depois de cada atividade, anote caso válido,
caso inválido e resultado observado. Continue para [depuração](04-evoluindo-o-projeto.md).
