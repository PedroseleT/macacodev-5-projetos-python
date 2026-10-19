# 🐒 MacacoDev | 5 Projetos Python para Sair do Tutorial

**Pare de apenas assistir aulas. Aprenda a construir projetos reais, passo a passo.**

O [MacacoDev](https://www.instagram.com/macacodev/) ensina programação de forma
acessível, com exemplos, humor e espaço para errar. Esta trilha gratuita foi feita
para quem conhece alguns conceitos, mas trava diante de um arquivo em branco.

> Você não aprende programação apenas assistindo. Você aprende tentando, errando,
> entendendo e construindo.

## [Comece por aqui →](COMECE-AQUI.md)

Você terá um esqueleto executável, atividades progressivas, dicas em camadas,
testes e uma solução de referência em cada projeto. Tente antes de consultar a
solução; depois explique o que mudou e construa uma versão sua.

| Ordem | Projeto | Nível | Estudo estimado* | Conceitos principais |
|---|---|---|---|---|
| 1 | [Desperdício Zero](01-desperdicio-zero/README.md) | Iniciante | 6–10 sessões | Funções, listas, dicionários, datas, JSON |
| 2 | [BuscaCEP Inteligente](02-buscacep/README.md) | Iniciante a intermediário | 5–8 sessões | Strings, HTTP, JSON, exceções, mocks |
| 3 | [OrçaDev](03-orcadev/README.md) | Intermediário | 6–10 sessões | Modelagem, Decimal, propostas e arquivos |
| 4 | [Fila Justa](04-fila-justa/README.md) | Intermediário | 6–9 sessões | FIFO, prioridade, estados e persistência |
| 5 | [Radar de Vagas Dev](05-radar-de-vagas/README.md) | Desafio final | 8–12 sessões | CRUD, filtros, estatísticas, CSV e testes |

*Estimativas de sessões de 45–90 minutos, não prazos nem condições de aprovação.
Avance quando conseguir explicar e modificar o programa. O [guia de estudos](GUIA-DE-ESTUDOS.md)
apresenta critérios de conclusão e uma sugestão flexível de organização.

## Instalação e primeira execução

Requer **Python 3.11 ou superior**. Sem pacotes externos, conta paga ou chave de API.
O BuscaCEP usa internet somente para a consulta real; todos os testes são offline.

Baixe em **Code → Download ZIP**, extraia e abra um terminal na pasta extraída.
Ou use Git:

```sh
git clone https://github.com/PedroseleT/macacodev-5-projetos-python.git
cd macacodev-5-projetos-python
python --version
python 01-desperdicio-zero/codigo-inicial/main.py
```

No macOS/Linux, se o comando for `python3`, substitua `python` em todos os exemplos.
No Windows também é possível usar `py -3`. Verifique se a versão é pelo menos 3.11.
Espaços nos nomes das pastas exigem aspas no terminal.

Para experimentar a referência funcional:

```sh
python 01-desperdicio-zero/solucao/main.py
python 02-buscacep/solucao/main.py
python 03-orcadev/solucao/main.py
python 04-fila-justa/solucao/main.py
python 05-radar-de-vagas/solucao/main.py
```

## Como estudar

1. Leia o problema e planeje entradas, saídas e regras no papel.
2. Entre em `codigo-inicial/`, execute o menu e implemente uma tarefa por vez.
3. Teste casos normais e inválidos. Consulte `dicas.md` aos poucos.
4. Compare com `solucao/` somente depois da tentativa; reescreva sem olhar.
5. Escolha um desafio e registre sua mudança em um commit.

O código inicial informa o que falta sem fingir que já salva ou consulta dados.
Os testes automatizados validam a solução; cada projeto explica como apontá-los
para sua implementação quando você reproduzir a mesma interface de funções.

## Organização

```text
macacodev-5-projetos-python/
├── COMECE-AQUI.md, GUIA-DE-ESTUDOS.md, COMO-USAR-GIT-E-GITHUB.md
├── COMO-CONTRIBUIR.md, LICENSE, VALIDACAO.md
├── assets/                       identidade visual original
├── scripts/                      testes e verificação de links
├── .github/                      integração contínua e modelos de issue
├── 01-desperdicio-zero/
├── 02-buscacep/
├── 03-orcadev/
├── 04-fila-justa/
└── 05-radar-de-vagas/
    ├── README.md, desafios.md, dicas.md, checklist.md
    ├── codigo-inicial/           ponto de partida para suas tentativas
    ├── solucao/                  main.py e pacote com módulos independentes
    ├── passo-a-passo/            cinco tutoriais
    └── testes/                  unittest, arquivos temporários e simulações
```

Cada projeto usa sua própria pasta `dados/`. Os aplicativos não compartilham estado.
O argumento `--dados CAMINHO` permite escolher outro JSON. Não abra duas instâncias
gravando o mesmo arquivo. Saiba como fazer backup e recuperar arquivos no README
do projeto antes de apagar ou editar dados.

## Testes e qualidade

Na raiz do repositório:

```sh
python scripts/testar.py
python scripts/verificar_documentacao.py
python -m compileall -q 01-desperdicio-zero 02-buscacep 03-orcadev 04-fila-justa 05-radar-de-vagas scripts
```

Cada suíte também pode rodar isoladamente, conforme seu README. A integração
contínua executa testes no Windows, Ubuntu e macOS com Python 3.11 e 3.13.
Consulte [VALIDACAO.md](VALIDACAO.md) para distinguir verificações locais de CI.

## Dúvidas, colaboração e portfólio

- [Guia de estudos](GUIA-DE-ESTUDOS.md)
- [Git e GitHub desde o início](COMO-USAR-GIT-E-GITHUB.md)
- [Como contribuir e abrir uma issue](COMO-CONTRIBUIR.md)
- [Dúvidas e relatos de erro](https://github.com/PedroseleT/macacodev-5-projetos-python/issues)
- [Licença MIT](LICENSE): mantenha os créditos e descreva o que você adaptou.

Projetos locais educacionais, sem autenticação, múltiplos usuários ou garantia de
backup. Não armazene senhas, documentos pessoais ou dados de clientes reais nos
exemplos públicos. A Fila Justa usa uma política didática, sem certificar atendimento
à legislação. O Radar organiza candidaturas inseridas manualmente, sem scraping.
