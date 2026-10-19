# Como contribuir

Use português brasileiro, exemplos pequenos e decisões que um iniciante consiga
acompanhar. Uma contribuição pode corrigir um link, explicar melhor um erro ou
adicionar um teste; não precisa começar com uma funcionalidade grande.

## Dúvida ou defeito

Abra [uma issue](https://github.com/PedroseleT/macacodev-5-projetos-python/issues/new/choose).
Informe projeto, sistema operacional, versão do Python, comando, entrada, resultado
esperado e resultado recebido. Apague nomes reais, links privados e informações
pessoais antes de anexar arquivos. Use os modelos disponibilizados no GitHub.

## Alteração de código ou documentação

1. Faça um fork e uma branch como no [guia de Git](COMO-USAR-GIT-E-GITHUB.md).
2. Reproduza o problema; para um defeito, acrescente um teste que falhe antes.
3. Mantenha interface, regras e persistência separadas. Use biblioteca padrão.
4. Execute `python scripts/testar.py` e `python scripts/verificar_documentacao.py` na raiz.
5. Execute `git diff --check` e confira se nenhum dado pessoal entrou no diff.
6. Abra um Pull Request com o motivo, resultado e testes realmente executados.

Soluções novas devem funcionar em Python 3.11+, usar `pathlib`, nomes em português
e funções compreensíveis. Docstrings orientam decisões, não narram cada atribuição.
Se usar uma ferramenta de IA, revise, execute e explique o código: a responsabilidade
pela contribuição continua sendo de quem a envia.

Os desafios são atividades para praticar. Evite publicar respostas completas em
issues de dicas; primeiro descreva sua tentativa e a dúvida específica.
