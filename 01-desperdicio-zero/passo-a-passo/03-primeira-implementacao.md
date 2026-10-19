# 3. Hora de colocar a mão no código

Abra a pasta `codigo-inicial` deste projeto no editor. Ela tem dois arquivos:
`main.py` mostra o menu; `tarefas.py` guarda orientações sobre o que falta construir.
O menu ainda não cadastra alimentos: essa parte será sua.

No terminal, a partir da pasta principal da trilha, rode:

```sh
python 01-desperdicio-zero/codigo-inicial/main.py
```

Se seu computador usa `python3` ou `py`, troque apenas a primeira palavra.

## Primeiro: um cadastro

Em `tarefas.py`, crie uma função para receber nome e quantidade e devolver um
dicionário. Comece com valores escritos no código. Depois acrescente as perguntas
com `input` no menu e chame sua função.

Lembre: o que vem de `input` é texto. Para calcular com a quantidade, será
necessário transformar esse texto em número. Se a pessoa escrever “seis”,
mostre uma mensagem e deixe tentar novamente.

## Depois: mais de um alimento

Crie uma lista que continue existindo enquanto o menu estiver aberto. Acrescente
o novo alimento nela e use `for` para mostrar um de cada vez. Cadastre Banana e
Arroz: os dois devem aparecer, sem um apagar o outro.

## Agora entram as datas

Use `datetime.strptime(texto, "%d/%m/%Y").date()` para transformar o texto em
uma data. Subtrair duas datas permite descobrir quantos dias faltam.
Uma data impossível, como 31/02, deve receber uma explicação na tela.

Por último, acrescente a remoção pelo ID e salve os dados em JSON, um arquivo
de texto organizado que Python consegue escrever e ler com o módulo `json`.
Use `pathlib.Path` para indicar o arquivo. Ao reabrir, carregue a lista salva.

Não tente terminar tudo de uma vez. Faça uma mudança, rode, observe e continue.

[Anterior: organizar](02-planeje-a-solucao.md) · [Próximo: quando algo dá errado](04-evoluindo-o-projeto.md)
