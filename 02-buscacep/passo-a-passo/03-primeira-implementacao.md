# 3. Vamos buscar um endereço

Abra os arquivos de `codigo-inicial`. O `main.py` mostra um menu; o `tarefas.py`
traz orientações para você substituir, aos poucos, por funções suas. Rode pela
pasta principal da trilha:

```sh
python 02-buscacep/codigo-inicial/main.py
```

## Comece sem usar a internet

Faça uma função que recebe o CEP e confere o formato. Aceite oito dígitos,
com ou sem o hífen na posição certa. Não “conserte” um texto cheio de letras:
explique que a pessoa precisa informar um CEP.

Experimente escrever `01001-000` e depois `123`. Só o primeiro deve continuar.

## Entenda uma resposta pequena

Antes da consulta, veja como Python lê JSON:

```python
import json

resposta = '{"localidade": "São Paulo", "uf": "SP"}'
endereco = json.loads(resposta)
print(endereco["localidade"])
```

A saída é `São Paulo`. `json.loads` transformou o texto em um dicionário.
É assim que conseguiremos acessar cada informação da resposta.

## Agora faça o pedido

Use `urlopen`, de `urllib.request`, com `timeout=10`. Esse limite evita esperar
para sempre. Leia a resposta, transforme os bytes em texto com `decode("utf-8")`
e passe esse texto para `json.loads`.

Peça o CEP conferido, mostre rua, bairro, cidade e estado. Se vier `{"erro": true}`,
avise que o CEP não foi encontrado.

Só depois conecte tudo ao menu e acrescente o histórico. Salve apenas consultas
válidas. Saia e abra novamente: consultar o histórico deve mostrar o que já foi
salvo, sem fazer outra chamada ao ViaCEP.

[Anterior: organizar](02-planeje-a-solucao.md) · [Próximo: quando a consulta falha](04-evoluindo-o-projeto.md)
