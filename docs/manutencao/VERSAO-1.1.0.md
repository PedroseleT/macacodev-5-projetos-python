# v1.1.0: um começo mais simples para quem está aprendendo

Esta versão revisa a apresentação e os textos da trilha. Os cinco programas
continuam com as mesmas funcionalidades.

- Página inicial com um caminho de entrada claro para quem nunca usou GitHub.
- Download sem exigir conta ou Git, extração do ZIP e preparação explicadas.
- Apresentação de cada projeto com o próximo passo em destaque.
- Vinte e cinco etapas reescritas em linguagem mais próxima e exemplos menores.
- Links de anterior e próximo para acompanhar as explicações em ordem.
- Dicas que abrem por assunto, desafios opcionais e revisões sem cobrança de testes.
- Git e publicação apresentados como um próximo passo, não uma condição para começar.
- Verificações automatizadas e relatórios técnicos preservados na área de manutenção.

O código de referência e os testes de manutenção foram preservados.
Nenhum dado de quem usa os programas está incluído no pacote.

## Conferências desta revisão

Executadas no Windows com Python 3.13.9:

- `python scripts/testar.py`: 79 verificações, nenhuma falha ou erro.
- `python scripts/verificar_documentacao.py`: 179 links locais, nenhum inválido.
- `python -m ruff check .`: nenhuma ocorrência.
- `python -m ruff format --check .`: 104 arquivos já formatados.
- `git diff --check`: nenhuma ocorrência.

Ruff 0.17.1 foi executado no ambiente de desenvolvimento `.venv`,
que não faz parte do pacote. O estudante não precisa instalar Ruff.

[Voltar à trilha](../../README.md) · [Área de manutenção](README.md)
