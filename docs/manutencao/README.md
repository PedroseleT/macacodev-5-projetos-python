# Informações para quem mantém o projeto

Se você veio estudar Python, pode deixar esta parte para depois.
[O caminho para começar está aqui](../../COMECE-AQUI.md).

Os testes automatizados continuam no repositório para conferir se as soluções
funcionam após uma alteração. Eles são uma ferramenta de manutenção, não uma
tarefa exigida de quem está escrevendo o primeiro programa.

## Conferir uma alteração

Na pasta principal do repositório:

```sh
python scripts/testar.py
python scripts/verificar_documentacao.py
python -m compileall -q 01-desperdicio-zero 02-buscacep 03-orcadev 04-fila-justa 05-radar-de-vagas scripts
git diff --check
```

Para conferir somente um aplicativo, por exemplo:

```sh
cd 01-desperdicio-zero
python -m unittest discover -s testes -v
```

O comando da raiz reúne todas as verificações. Os testes importam a solução
de referência, não o código que o estudante escreve em `codigo-inicial`.
O BuscaCEP usa respostas simuladas, sem depender de conexão para esses testes.
O GitHub Actions também verifica os programas em Windows, Linux e macOS.

## Detalhes que não precisam aparecer na primeira leitura

- Cada projeto salva seus próprios dados. O argumento `--dados` permite escolher
  outro JSON. O caminho padrão parte do local do programa, não da pasta do terminal.
- Arquivos inválidos são preservados, com encerramento de abertura em código 1.
- A gravação usa um temporário e substitui o destino depois de escrever.
  Isso não permite várias instâncias editando o mesmo JSON nem substitui backups.
- `deepcopy` prepara um estado separado: uma operação inválida não deve alterar
  parcialmente o estado atual. Os testes conferem esse comportamento.
- Um `main.py` abre cada aplicativo. Importar seus módulos não abre o menu.
- Os preços do OrçaDev usam Decimal criado de texto; JSON guarda valores como strings.
- Datas de eventos usam ISO com fuso. Datas informadas pelo usuário seguem o formato
  DD/MM/AAAA e são salvas como AAAA-MM-DD.
- O Radar protege células de fórmula no CSV sem mudar os textos originais no JSON.

[O que mudou na leitura da trilha](VERSAO-1.1.0.md)

[Resultados da primeira versão](VALIDACAO.md) · [Entrega inicial](ENTREGA.md)
· [Histórico v1.0.0](VERSAO-1.0.0.md) · [Como contribuir](../../COMO-CONTRIBUIR.md)
