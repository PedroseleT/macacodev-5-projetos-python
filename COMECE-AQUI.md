# Sua primeira execução

Você não precisa saber tudo antes de começar. Precisa reconhecer texto, números,
`if`, `for`, listas e a ideia de função. Se algum conceito estiver novo, execute
um exemplo pequeno antes de avançar.

## 1. Prepare o ambiente

Instale Python 3.11+ pelo [site oficial](https://www.python.org/downloads/).
No Windows, marque a opção de adicionar Python ao PATH durante a instalação.
Feche e abra o terminal depois de instalar. No macOS/Linux, experimente `python3`.

```sh
python --version
```

Se aparecer “comando não encontrado”, confira a instalação e o PATH. Não cole esse
comando dentro do interpretador que mostra `>>>`; digite `exit()` para voltar ao
terminal do sistema. Abra um editor, por exemplo IDLE (incluído no Python) ou VS Code.

## 2. Baixe e localize a pasta

No GitHub: **Code → Download ZIP → Extrair tudo**. O navegador não executa Python.
Abra a pasta extraída no editor e abra o terminal nessa pasta. `dir` (Windows) ou
`ls` (macOS/Linux) deve mostrar `README.md` e os cinco projetos.

Opcionalmente, com Git instalado:

```sh
git clone https://github.com/PedroseleT/macacodev-5-projetos-python.git
cd macacodev-5-projetos-python
```

## 3. Comece pelo esqueleto

```sh
python 01-desperdicio-zero/codigo-inicial/main.py
```

O menu abre, mas as tarefas ainda não estão implementadas. Isso é intencional.
Leia [o primeiro problema](01-desperdicio-zero/passo-a-passo/01-entenda-o-problema.md),
planeje uma lista de alimentos e tente cadastrar um item apenas em memória.
Você ainda não precisa escrever JSON.

## 4. Faça uma experiência controlada

Depois da tentativa, você pode experimentar a solução com dados descartáveis:

```sh
python 01-desperdicio-zero/solucao/main.py --dados 01-desperdicio-zero/dados/experimento.json
```

Cadastre um alimento com validade futura, liste, saia com `0` e abra novamente.
O item deve continuar lá. Não use dados pessoais. Os arquivos de `dados/` ficam
fora do Git. O programa informa erros sem apagar um arquivo corrompido.

## 5. Confira uma mudança

```sh
cd 01-desperdicio-zero
python -m unittest discover -s testes -v
```

`OK` significa que aqueles cenários passaram, não que todo comportamento possível
foi provado. Se falhar, leia primeiro o nome do teste e a última linha do erro.
Depois volte ao [guia de estudos](GUIA-DE-ESTUDOS.md).
