# 1. Desperdício Zero 🍌

**Sabe aquela banana que você comprou e só lembrou quando já estava passando?**

Neste primeiro projeto, vamos criar uma lista de alimentos no computador.
Você vai anotar o nome, a quantidade e a validade, e o programa vai mostrar
o que está perto de vencer. Uma ideia simples para começar a juntar o que aprendeu.

### [Começar a primeira etapa: entender a ideia →](passo-a-passo/01-entenda-o-problema.md)

Se ainda não preparou o computador, [passe aqui primeiro](../COMECE-AQUI.md).

## Como vai ficar?

Imagine cadastrar seis bananas com uma data de validade. Depois, ao pedir para
ver a lista, aparece algo assim:

```text
Banana | quantidade: 6 | validade: 20/10/2026
```

Você também poderá ver só os alimentos que venceram ou os que vencem em breve,
remover um item e fechar o programa. Quando abrir de novo, a lista continuará lá.

## O que você vai aprender pelo caminho

A guardar informações, repetir uma ação, organizar uma lista e dividir o programa
em funções: pequenos blocos que fazem uma tarefa. Mais adiante, vamos salvar
as informações em um arquivo para elas não sumirem quando você sair.

Conhecer um pouco de variáveis, `if` e repetição já ajuda. Você não precisa
saber mexer com datas e arquivos antes: a explicação chega na hora de usar.

## Siga as etapas nessa ordem

1. [O que vamos criar e por quê](passo-a-passo/01-entenda-o-problema.md)
2. [Separando a ideia em partes menores](passo-a-passo/02-planeje-a-solucao.md)
3. [Hora de escrever, um pedaço de cada vez](passo-a-passo/03-primeira-implementacao.md)
4. [Deu erro? Vamos entender](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Agora deixe o projeto com a sua cara](passo-a-passo/05-finalizacao.md)

Cada página termina com um link para a próxima. Você não precisa voltar aqui
para procurar por onde continuar.

[Precisa de uma dica?](dicas.md) · [Ideias para continuar](desafios.md)
· [O que já consegui fazer?](checklist.md)

<details><summary>Quero experimentar o programa pronto</summary>

No terminal, dentro da pasta principal que contém os cinco projetos:

```sh
python 01-desperdicio-zero/solucao/main.py
```

Escolha `1` para cadastrar, `2` para listar ou `0` para sair. Digite a validade
como `20/10/2026`. O nome pode incluir uma unidade, como “Arroz (kg)”.
Para este exercício, próximo do vencimento significa de hoje até três dias
à frente. Uma data anterior a hoje aparece como vencida. O programa organiza
datas; ele não avalia se um alimento está próprio para consumo.

Depois, volte à sua tentativa. A versão pronta é uma ajuda para comparar,
não uma etapa que você precisa decorar.

</details>

<details><summary>Onde a minha lista fica salva?</summary>

A versão pronta cria `dados/alimentos.json` dentro da pasta deste projeto.
JSON é um jeito de escrever informações organizadas em um arquivo de texto.
Não precisa editar esse arquivo para usar o programa.

Se quiser uma cópia de segurança, feche o programa e copie esse arquivo.
Se aparecer um aviso de arquivo com problema, não apague a única cópia:
guarde o original antes de tentar corrigir ou recuperar um backup.
Use uma janela do programa por vez para não misturar gravações.

</details>

[Voltar à página inicial](../README.md) · [Como pedir ajuda](../COMO-CONTRIBUIR.md)
