# Histórico: MacacoDev — 5 Projetos Python · v1.0.0

Primeira versão pública da trilha para sair do tutorial e construir projetos.

## Aplicações incluídas

- Desperdício Zero: alimentos, quantidades, validade, alertas e JSON.
- BuscaCEP Inteligente: ViaCEP com urllib, erros tratados e histórico local.
- OrçaDev: clientes, serviços, Decimal, desconto e propostas em TXT/JSON.
- Fila Justa: filas FIFO, prioridade didática 2:1 e recuperação de atendimento.
- Radar de Vagas Dev: CRUD, filtros, pesquisa, estatísticas, JSON e CSV.

## Material para estudar

Cinco códigos iniciais independentes das soluções, 25 tutoriais, desafios em três
níveis, dicas progressivas, checklists, guia de estudos e introdução a Git/GitHub.
Documentação e menus em português brasileiro; licença MIT.

## Verificação

79 testes passaram localmente e nos seis ambientes de CI: Python 3.11/3.13 em
Windows, Ubuntu e macOS. Lint, formatação, compilação e links internos verificados.
Testes de API totalmente offline; uma consulta real ao ViaCEP foi conferida à parte.

## Para começar

Extraia o ZIP, instale Python 3.11+ e abra COMECE-AQUI.md. Na pasta extraída:

```sh
python 01-desperdicio-zero/codigo-inicial/main.py
python scripts/testar.py
```

Os aplicativos não precisam de pip, contas, chaves ou banco externo. Somente a
consulta real de CEP precisa de internet. Use uma instância por arquivo de dados
e mantenha backups locais. Não inclua dados pessoais nas adaptações publicadas.
