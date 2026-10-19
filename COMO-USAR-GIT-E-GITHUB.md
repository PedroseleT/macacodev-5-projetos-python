# Quero colocar minha versão no GitHub. Como faço?

Esta parte pode esperar até você ter um programa que queira compartilhar.
Para baixar a trilha e aprender Python, basta seguir o [Comece aqui](COMECE-AQUI.md).

## Primeiro: quem é quem?

**GitHub** é o site onde você está lendo o projeto. Uma pasta de projeto guardada
ali é chamada de **repositório**.

**Git** é uma ferramenta que registra versões dos arquivos no computador.
Você pode pensar nessas versões como pontos de um histórico: cada uma tem
uma mensagem dizendo o que mudou.

Não precisa aprender todos os comandos de uma vez. Vamos escolher um caminho
de acordo com o que você quer fazer.

## Só quero estudar

Baixe o ZIP, extraia e siga a trilha. Não precisa criar conta, instalar Git
ou publicar nada para acompanhar os projetos.

## Quero mostrar minha própria adaptação

Você pode começar pelo próprio site do GitHub, sem comandos de Git:

1. Crie uma conta ou entre na sua.
2. Use o botão **+** no alto da página e escolha **New repository**.
3. Dê um nome, como `meu-controle-de-alimentos`, e escreva uma descrição curta.
4. Escolha **Public** se quiser que outras pessoas vejam e crie o repositório.
5. Use **Add file → Upload files** para enviar os arquivos da sua versão.
   Numa página vazia, procure o link **uploading an existing file**.
6. Escreva uma mensagem curta sobre o envio e confirme em **Commit changes**.

Esses nomes podem variar um pouco conforme o idioma da sua conta.

**O que enviar:** o código do projeto que você adaptou, um README explicando
como executar e a licença MIT da base. Cite o MacacoDev e conte o que você mudou.
Mantenha a organização de pastas que seu comando de execução precisa.

**O que deixar de fora:** arquivos de `dados`, senhas, contatos de clientes,
currículos, `__pycache__` e qualquer informação pessoal. Antes de confirmar,
olhe a lista de arquivos que será publicada.

O envio pelo site não aplica seu `.gitignore` automaticamente: revise os arquivos
mesmo que essa lista de coisas ignoradas já exista no computador.

## Quero aprender Git aos poucos

<details><summary>1. Baixar pelo Git, em vez do ZIP</summary>

Instale pelo [site oficial do Git](https://git-scm.com/downloads) e abra um novo
terminal. Depois:

```sh
git --version
git clone https://github.com/PedroseleT/macacodev-5-projetos-python.git
cd macacodev-5-projetos-python
git status
```

`clone` baixa uma cópia com o histórico; `status` mostra se você mudou arquivos.
Isso ainda não envia nada para a internet.

</details>

<details><summary>2. Criar uma cópia na minha conta para contribuir</summary>

No projeto original, use **Fork → Create fork**. Fork é uma cópia na sua conta.
Na página dessa cópia, use **Code** e copie a URL HTTPS.

No terminal, substitua `URL_DO_SEU_FORK` por essa URL:

```sh
git clone URL_DO_SEU_FORK
cd macacodev-5-projetos-python
git switch -c minha-melhoria
```

O último comando cria uma **branch**: um espaço separado no histórico para
trabalhar na mudança. Não digite o marcador de URL literalmente.

</details>

<details><summary>3. Guardar uma mudança e enviar</summary>

Configure um nome público e o e-mail que será mostrado nos registros. Para
proteger seu e-mail pessoal, use o endereço **noreply** disponível em
**Settings → Emails** na sua conta do GitHub. Substitua os exemplos:

```sh
git config --global user.name "Seu nome publico"
git config --global user.email "SEU_EMAIL_NOREPLY_DO_GITHUB"
```

Depois de mudar um arquivo, confira o que será enviado:

```sh
git status
git diff
git add README.md
git diff --cached
git commit -m "Melhora a explicacao para comecar"
git push -u origin minha-melhoria
```

Esse exemplo prepara só o `README.md`. Troque o caminho se mudou outro arquivo.

`add` escolhe o arquivo; `commit` registra a versão local com uma mensagem;
`push` envia para sua cópia no GitHub. Salvar no editor não faz esses passos
automaticamente. O GitHub pode pedir autenticação no navegador: nunca coloque
senha ou token dentro de um arquivo ou de um link compartilhado.

</details>

## Quero ajudar a melhorar a trilha

Uma **issue** é uma mensagem pública sobre uma dúvida ou problema.
Um **Pull Request** é uma proposta de alteração nos arquivos.

Depois de enviar uma mudança ao seu fork, o GitHub costuma oferecer
**Compare & pull request**. Explique o que mudou e por quê.
O [guia de contribuição](COMO-CONTRIBUIR.md) ajuda com essa parte.

Se um comando der erro, leia a mensagem e peça ajuda antes de tentar forçar
um envio. Não precisa arriscar apagar seu trabalho para aprender.

[Voltar à trilha](README.md)
