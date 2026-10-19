# 4. Deu erro? Vamos descobrir juntos

O programa rodar de primeira seria ótimo, mas erro faz parte. O importante é
descobrir em qual pedacinho ele começou, em vez de mudar dez coisas ao mesmo tempo.

## A quantidade não vira número

Se você digitou “duas”, Python não consegue transformar isso em um número.
Pode aparecer `ValueError`. Essa mensagem não significa que perdeu o projeto:
significa que aquela conversão não funcionou.

Use `try` e `except ValueError` ao fazer a conversão. No `except`, explique
“Digite uma quantidade em números” e permita outra tentativa. Quantidade zero
ou negativa também precisa de uma mensagem, mesmo sendo um número.

## A data parece certa, mas não existe

31/02 tem o formato esperado, mas fevereiro não tem esse dia. A conversão de datas
do Python percebe isso. Evite tentar resolver contando só os caracteres do texto.

## Sumiu o alimento errado

Olhe o ID de cada alimento antes da remoção. O número próprio do alimento não
é a mesma coisa que sua posição na lista. A posição muda quando alguém sai;
o ID dos outros alimentos deve continuar igual.

## Um jeito simples de investigar

Coloque `print(alimentos)` antes e depois da parte que parece errada. Veja o que
mudou. Depois que entender, retire essas mensagens extras.

Se aparecer um texto grande de erro, comece pela última linha: ela costuma indicar
o tipo de problema. Procure também a linha do seu arquivo mencionada acima dela.

Nunca apague automaticamente um arquivo que falhou ao abrir. Faça uma cópia antes
de tentar corrigir: não queremos trocar um pequeno erro por uma lista perdida.

[Anterior: construir](03-primeira-implementacao.md) · [Próximo: deixar com a sua cara](05-finalizacao.md)
