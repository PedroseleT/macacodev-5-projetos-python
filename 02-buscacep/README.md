# 2. BuscaCEP Inteligente 📍

**Você digita o CEP e o programa descobre a rua, o bairro, a cidade e o estado.**

Já viu um formulário completar o endereço depois que você informa o CEP?
Vamos construir uma versão pequena dessa ideia. Aqui a novidade é buscar uma
informação na internet, em vez de pedir que a pessoa digite tudo.

### [Começar: entender como a consulta funciona →](passo-a-passo/01-entenda-o-problema.md)

É mais fácil acompanhar depois do [primeiro projeto](../01-desperdicio-zero/README.md).

## Como vai ficar?

```text
Digite um CEP: 01001-000

Rua: Praça da Sé
Bairro: Sé
Cidade: São Paulo
Estado: SP
```

Esse é um endereço público usado como exemplo pelo [ViaCEP](https://viacep.com.br/),
o serviço gratuito que vamos consultar. A base dele pode ser atualizada.
Você pode digitar com ou sem hífen, fazer outras consultas e ver as anteriores.

## O que você vai aprender

A conferir um texto antes de usar, pedir informações a outro programa e mostrar
uma mensagem útil quando algo não der certo. Uma consulta pode falhar porque
o CEP não existe ou porque a conexão caiu, por exemplo.

Você vai encontrar a palavra **API**: é uma forma de programas conversarem.
A gente explica isso com calma antes de fazer a consulta. Não precisa decorar
siglas nem criar conta em serviço nenhum.

## Seu caminho

1. [Entenda o que vamos buscar](passo-a-passo/01-entenda-o-problema.md)
2. [Pense no pedido e na resposta](passo-a-passo/02-planeje-a-solucao.md)
3. [Faça a primeira consulta por partes](passo-a-passo/03-primeira-implementacao.md)
4. [E se a internet ou o CEP não ajudar?](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Escolha sua próxima melhoria](passo-a-passo/05-finalizacao.md)

[Precisa de uma dica?](dicas.md) · [Ideias para continuar](desafios.md)
· [O que já consegui fazer?](checklist.md)

<details><summary>Quero abrir a versão pronta</summary>

No terminal, na pasta principal dos cinco projetos:

```sh
python 02-buscacep/solucao/main.py
```

Escolha `1` para consultar, `2` para ver o histórico ou `0` para sair.
Uma consulta nova precisa de internet. Ver o que já foi salvo não precisa.
CEP de município pode vir sem rua ou bairro; nesse caso, o programa mostra
que o campo não foi informado.

</details>

<details><summary>Onde ficam as consultas anteriores?</summary>

Em `dados/historico.json`, dentro deste projeto. Cada consulta que deu certo
fica registrada com data e hora. Consultar o mesmo CEP novamente cria outro
registro. Uma consulta que falhou não entra na lista.

Feche o programa antes de copiar o arquivo como backup. Se ele tiver um
problema, o programa avisa sem apagar seu conteúdo. Preserve uma cópia antes
de tentar corrigir. Use uma janela por vez e faça consultas individuais:
o ViaCEP não é para baixar uma base inteira de endereços.

</details>

[Voltar ao início](../README.md) · [Como pedir ajuda](../COMO-CONTRIBUIR.md)
