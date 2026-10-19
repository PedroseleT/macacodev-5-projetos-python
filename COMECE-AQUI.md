# Chegou agora? Bora começar 🐒

Se você nunca estudou por um projeto do GitHub, essa página é pra você.
Vamos baixar os arquivos, preparar o computador e abrir o primeiro projeto.
**Não precisa mexer em Git, criar conta ou ler todas as pastas agora.**

## 1. Baixe os arquivos

[Clique aqui para baixar o projeto completo em ZIP](https://github.com/PedroseleT/macacodev-5-projetos-python/archive/refs/heads/main.zip).

ZIP é um pacote com as pastas dentro. Quando terminar o download:

1. Vá até a pasta de downloads do computador.
2. Clique com o botão direito no ZIP e escolha **Extrair tudo** ou **Extrair aqui**.
3. Abra a pasta extraída. Se tiver outra pasta dentro, abra também, até encontrar
   este arquivo e as pastas `01-desperdicio-zero`, `02-buscacep` e as demais.

Não execute os arquivos de dentro do ZIP: extraia primeiro. Você pode deixar a
pasta na Área de Trabalho ou em Documentos, onde for mais fácil encontrar.

## 2. Confira se o Python está instalado

Python é quem vai executar o código que você escrever.
Se ainda não instalou, baixe pelo [site oficial do Python](https://www.python.org/downloads/)
e instale a versão 3.11 ou mais recente. No Windows, marque **Add Python to PATH**
se essa opção aparecer no instalador. Depois, feche e abra o terminal.

**O que é terminal?** É uma janela onde você digita comandos para o computador.
Não é um arquivo de código e não é a caixa de pesquisa do navegador.

Para abrir nessa pasta:

- **Windows:** no Explorador de Arquivos, abra a pasta extraída, clique na barra
  que mostra o caminho lá em cima, digite `powershell` e aperte Enter.
- **macOS:** abra o Terminal, digite `cd` seguido de um espaço, arraste a pasta
  extraída para a janela e aperte Enter.
- **Linux:** na pasta extraída, procure a opção **Abrir no terminal** no botão
  direito. O nome pode variar conforme a distribuição.

Agora digite e aperte Enter:

```sh
python --version
```

Se aparecer algo como `Python 3.13.9`, está certo. Precisa ser 3.11 ou mais recente.
No macOS/Linux, talvez o comando seja `python3 --version`. Nesse caso, use
`python3` no lugar de `python` nos exemplos. No Windows, `py --version` também
pode funcionar; se usar `py`, mantenha esse nome nos comandos seguintes.

## 3. Escolha onde escrever o código

Use o editor que você já conhece. Se não tiver um, o **IDLE** costuma vir com a
instalação do Python e já permite abrir e editar arquivos `.py`.
Esses arquivos são os textos onde escrevemos as instruções do programa.

Não precisa instalar um monte de ferramentas para acompanhar. Se você já usa
VS Code, pode continuar nele normalmente.

## 4. Vá para o primeiro projeto

### [Abrir o Desperdício Zero →](01-desperdicio-zero/README.md)

Primeiro você vai entender o que vamos criar. Depois, a explicação mostra qual
arquivo abrir e qual comando digitar. Deixe o terminal na pasta principal que
contém os cinco projetos; os comandos do passo a passo partem desse lugar.

Um detalhe importante: `codigo-inicial` tem um menu e orientações para começar.
Ele **ainda não faz o trabalho inteiro**. É você quem vai construir as ações com
ajuda das etapas. A versão pronta fica em `solucao`, para comparar depois.

## Deu algum problema na preparação?

<details><summary>O computador não reconhece python</summary>

Experimente `py --version` no Windows ou `python3 --version` no macOS/Linux.
Se nenhum funcionar, confira a instalação do Python. No Windows, abra o instalador
novamente para conferir a opção de adicionar Python ao PATH e abra um novo terminal.

</details>

<details><summary>Apareceu uma mensagem dizendo que não encontrou o arquivo</summary>

Você pode estar na pasta errada. Digite `dir` no Windows ou `ls` no macOS/Linux.
Precisa aparecer `01-desperdicio-zero`. Se só aparecer uma pasta com o nome do
projeto, entre nela primeiro. O nome pode terminar em `-main`: isso é normal.

</details>

<details><summary>Apareceu >>> e o comando deu erro</summary>

Você abriu o Python interativo. Digite `exit()` e aperte Enter para voltar ao
terminal. Os comandos que começam com `python` são digitados no terminal.

</details>

[Voltar à apresentação](README.md) · [Preciso de ajuda](COMO-CONTRIBUIR.md)
