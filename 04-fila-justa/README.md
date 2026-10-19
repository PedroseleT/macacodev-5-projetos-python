# 4. Fila Justa 🎟️

**Quem é o próximo? Vamos organizar um pequeno atendimento.**

Neste projeto, a pessoa pega uma senha, espera ser chamada e depois termina
o atendimento. Parece simples, mas o programa precisa lembrar quem está em
cada situação, inclusive quando você fecha e abre de novo.

### [Começar: conhecer a fila que vamos organizar →](passo-a-passo/01-entenda-o-problema.md)

## Como vai funcionar?

Teremos senhas comuns e prioritárias. Dentro de cada grupo, quem chegou
primeiro será chamado primeiro.

Para o exercício, quando houver pessoas nos dois grupos, a ordem será:

```text
Uma prioritária → outra prioritária → uma comum → repetir
```

Se só houver gente em um dos grupos, o atendimento continua com esse grupo.
Essa é uma regra escolhida para estudar programação, não uma garantia de que
o sistema atende todas as exigências legais de um estabelecimento.

## O que você vai construir

Um menu para gerar senhas, ver quem aguarda, chamar a próxima pessoa e terminar
um atendimento. Também poderá olhar o histórico e contar quantos terminaram.
Não vamos pedir nomes: os números das senhas já resolvem o exercício.

Você vai praticar listas, decisões com `if` e a ideia de guardar o que mudou
depois de cada ação. Não precisa conhecer estruturas complicadas para começar.

## Seu caminho

1. [Imagine o atendimento](passo-a-passo/01-entenda-o-problema.md)
2. [Separe quem espera, quem está sendo atendido e quem terminou](passo-a-passo/02-planeje-a-solucao.md)
3. [Construa uma ação de cada vez](passo-a-passo/03-primeira-implementacao.md)
4. [Descubra por que a fila saiu da ordem](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Crie uma melhoria sua](passo-a-passo/05-finalizacao.md)

[Precisa de uma dica?](dicas.md) · [Ideias para continuar](desafios.md)
· [O que já consegui fazer?](checklist.md)

<details><summary>Quero experimentar o atendimento pronto</summary>

No terminal, na pasta principal dos cinco projetos:

```sh
python 04-fila-justa/solucao/main.py
```

Escolha `1` para senha comum, `2` para prioritária, `3` para ver a fila,
`4` para chamar e `5` para concluir o atendimento. A opção `6` mostra o histórico,
`7` mostra as contagens e `0` sai. Conclua o atendimento atual antes de chamar outro.

As senhas têm letras e números, como `C0001` e `P0002`. O número é único,
mesmo entre grupos diferentes. Ele não é a posição atual da pessoa na fila.

</details>

<details><summary>Se eu fechar o programa, perco a fila?</summary>

A versão pronta salva em `dados/fila.json`, dentro deste projeto. Ela guarda
as duas filas, o atendimento atual e o histórico. Ao abrir de novo, continua
de onde estava. O arquivo é criado na primeira alteração.

Feche o programa antes de copiar o arquivo para um backup. Se houver um problema
na leitura, ele avisa sem apagar o original. Não apague o arquivo para tentar
resolver um erro sem antes guardar uma cópia. Use uma janela por vez.

</details>

[Voltar ao início](../README.md) · [Como pedir ajuda](../COMO-CONTRIBUIR.md)
