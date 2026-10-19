# Relatório técnico da entrega inicial · MacacoDev — 5 Projetos Python

Este documento registra a versão 1.0.0. A apresentação atual para estudantes está
na [página inicial](../../README.md). Os comandos abaixo partem da pasta principal.

## 1. Resumo do trabalho realizado

Cinco aplicações de terminal implementadas com biblioteca padrão do Python 3.11+,
105 arquivos na fundação inicial e material integral em português brasileiro.
Regras de negócio, interface e arquivos estão separados. Toda aplicação possui
código inicial independente, solução, cinco tutoriais, desafios, dicas e checklist.

A progressão parte de listas e datas, passa por uma API, precisão monetária e
estados de fila e termina num CRUD com filtros e CSV. O aluno é orientado a prever,
tentar, testar, depurar e personalizar antes de consultar a solução.

## 2. Estrutura do repositório

```text
macacodev-5-projetos-python/
├── README.md, COMECE-AQUI.md, GUIA-DE-ESTUDOS.md
├── COMO-USAR-GIT-E-GITHUB.md, COMO-CONTRIBUIR.md
├── LICENSE, VALIDACAO.md, NOTAS-DA-VERSAO.md, ENTREGA.md
├── .gitignore, .gitattributes, pyproject.toml
├── .github/                  CI, modelos de issue e Pull Request
├── assets/README.md          critérios da identidade visual
├── scripts/                 suíte conjunta e verificação de links
├── testes/                  primeira execução e preservação dos dados
├── 01-desperdicio-zero/
├── 02-buscacep/
├── 03-orcadev/
├── 04-fila-justa/
└── 05-radar-de-vagas/
    ├── README.md, desafios.md, dicas.md, checklist.md
    ├── codigo-inicial/main.py, tarefas.py
    ├── solucao/main.py
    ├── solucao/<pacote>/     módulos próprios de cada aplicativo
    ├── passo-a-passo/       cinco tutoriais em cada projeto
    └── testes/              suíte específica
```

## 3. Projetos implementados

| Aplicativo | Resultado funcional |
|---|---|
| Desperdício Zero | cadastra/lista/remove alimentos; valida quantidade/data; filtra vencidos/próximos; recupera JSON |
| BuscaCEP | valida CEP; consulta ViaCEP; mostra endereço; trata inexistência, conexão e resposta inesperada; mantém histórico |
| OrçaDev | cadastra clientes/serviços; calcula subtotal, desconto fixo e total com Decimal; salva/consulta/exporta propostas |
| Fila Justa | gera senhas de duas categorias; preserva FIFO; aplica 2:1; chama/conclui; historiza e conta; recupera estado completo |
| Radar de Vagas | cadastra, lista, filtra, pesquisa, atualiza e exclui; mantém sete status; exporta CSV e recupera JSON |

## 4. Testes realizados

79 testes: 12 + 15 + 12 + 13 + 16 dos aplicativos e 11 da trilha. Nenhuma falha,
erro ou teste ignorado na execução local em Windows/Python 3.13.9. A suíte também
passou em Python 3.11 e 3.13 no Windows, Ubuntu e macOS via GitHub Actions.

```sh
python scripts/testar.py
python scripts/verificar_documentacao.py
python -m compileall -q 01-desperdicio-zero 02-buscacep 03-orcadev 04-fila-justa 05-radar-de-vagas scripts
git diff --check
```

Ruff check e format --check também passaram. Os testes de BuscaCEP são offline.
Uma consulta real isolada ao CEP público 01001000 retornou São Paulo/SP. Um clone
limpo da publicação repetiu a suíte sem instalar dependências dos aplicativos.
Detalhes e execução de CI: [VALIDACAO.md](VALIDACAO.md).

## 5. Instruções de execução

Baixe o ZIP da release, extraia e abra [COMECE-AQUI.md](../../COMECE-AQUI.md). Ou:

```sh
git clone https://github.com/PedroseleT/macacodev-5-projetos-python.git
cd macacodev-5-projetos-python
python 01-desperdicio-zero/codigo-inicial/main.py
python 01-desperdicio-zero/solucao/main.py
```

Python 3.11+, sem pacotes obrigatórios. No macOS/Linux, `python3` pode substituir
`python`. Cada README documenta comando próprio, testes, menus e arquivos de dados.

## 6. Publicação

[Repositório público](https://github.com/PedroseleT/macacodev-5-projetos-python).
[Release v1.0.0](https://github.com/PedroseleT/macacodev-5-projetos-python/releases/tag/v1.0.0).
Licença MIT, créditos MacacoDev e ZIP sem ambiente virtual, dados pessoais ou cache.

## 7. Limitações conhecidas

- Somente uma instância por arquivo; não há banco multiusuário, sincronização ou login.
- JSON e TXT/CSV são gravações separadas; exportações são regeneráveis a partir do JSON.
- Escrita por substituição reduz falhas parciais, mas backups continuam necessários.
- ViaCEP é serviço externo; consulta real depende da sua disponibilidade e internet.
- Validação de link no Radar é sintática; não comprova que a vaga continua aberta.
- OrçaDev não é sistema fiscal e Fila Justa não certifica conformidade legal.
- Quantidades de serviços no OrçaDev são inteiras; fracionar horas é melhoria futura.
- Não há funções obrigatórias pendentes; desafios extras são atividades propostas,
  não funcionalidades anunciadas como implementadas.

## 8. Próximos passos

Testar o material com iniciantes reais para observar onde travam; melhorar os
enunciados a partir de dúvidas; acrescentar gravações curtas de terminal e
expansões opcionais como edição de alimentos, cache de CEP, desconto percentual,
múltiplos guichês e filtros por período. Essas melhorias não fazem parte da versão 1.
