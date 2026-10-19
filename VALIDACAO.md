# Validação da primeira versão

Verificação local em 18/10/2026: Windows, Python 3.13.9. A matriz de CI não deve
ser confundida com execução local: consulte o histórico do GitHub Actions para
confirmar cada ambiente.

## Resultados locais

| Verificação | Resultado |
|---|---|
| Desperdício Zero | 12 testes aprovados |
| BuscaCEP | 15 testes offline aprovados |
| OrçaDev | 12 testes aprovados |
| Fila Justa | 13 testes aprovados |
| Radar de Vagas | 16 testes aprovados |
| Integração e estrutura da trilha | 11 testes aprovados |
| Total | 79 testes, zero falhas, zero erros, zero ignorados |
| Links relativos Markdown | verificação automática sem destinos inválidos |
| Sintaxe | compileall sem erros; ast em modo Python 3.11 |
| Estilo | Ruff 0.17.1: check e format --check aprovados |
| ViaCEP real, fora da suíte | uma consulta de 01001000 retornou São Paulo/SP |

O lint foi executado num ambiente virtual local, não é uma dependência dos
aplicativos. Configuração em `pyproject.toml`. Para reproduzir opcionalmente:

```sh
python -m venv .venv
```

Windows:

```powershell
.venv/Scripts/python.exe -m pip install ruff==0.17.1
.venv/Scripts/python.exe -m ruff check .
.venv/Scripts/python.exe -m ruff format --check .
```

macOS/Linux:

```sh
.venv/bin/python -m pip install ruff==0.17.1
.venv/bin/python -m ruff check .
.venv/bin/python -m ruff format --check .
```

## Comandos reproduzíveis na raiz

```sh
python scripts/testar.py
python scripts/verificar_documentacao.py
python -m compileall -q 01-desperdicio-zero 02-buscacep 03-orcadev 04-fila-justa 05-radar-de-vagas scripts
git diff --check
```

As suítes usam unittest e dados temporários. BuscaCEP simula HTTP; não depende de
internet. Testes da trilha abrem os cinco menus por subprocessos, com diretório
de trabalho diferente e caminhos com espaços, e verificam a preservação de JSON
corrompido e UTF-8 inválido. O parser ast também verifica sintaxe disponível em 3.11;
isso complementa, mas não substitui executar a suíte nessa versão.

## Integração contínua executada

[Execução confirmada no GitHub Actions](https://github.com/PedroseleT/macacodev-5-projetos-python/actions/runs/39184586727),
commit `046ce3b`: sete jobs concluídos com sucesso. Cada um dos seis ambientes de
teste executou os mesmos 79 testes sem falhas:

| Sistema | Python 3.11 | Python 3.13 |
|---|---|---|
| Ubuntu | aprovado | aprovado |
| Windows | aprovado | aprovado |
| macOS | aprovado | aprovado |

O sétimo job verificou lint e formatação. Também foi feito clone público limpo em
outra pasta temporária no Windows: 79 testes aprovados e links válidos sem instalar
dependências dos aplicativos. Mudanças posteriores apenas de documentação são
verificadas novamente pelo workflow a cada push.
