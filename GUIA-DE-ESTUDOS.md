# Estude para conseguir construir

## Ordem e critérios

Comece no Desperdício Zero: você recebe uma entrada, representa um registro e salva
uma lista. No BuscaCEP, a entrada passa a vir também de um serviço externo. No
OrçaDev, você aprende regras monetárias. Na Fila Justa, decisões mudam um estado ao
longo de várias operações. No Radar, você combina tudo em um CRUD maior.

Antes de cada projeto, tente explicar `if`, `while`, função, lista e dicionário.
Antes do segundo, saiba abrir um arquivo e tratar `ValueError`. Antes do terceiro,
entenda a diferença entre texto numérico e número. Antes do quarto, consiga
acompanhar alterações em uma lista. Antes do quinto, consiga separar menu e regras.

Você concluiu uma etapa quando consegue: executar um caso válido, rejeitar um
inválido, explicar o motivo de uma decisão e modificar a regra sem copiar.

## Organização sugerida, sem prazo obrigatório

Use os intervalos de sessões da [tabela inicial](README.md) apenas como estimativa.
Um ciclo possível por semana tem três encontros: planejar e tentar; depurar e
testar; reconstruir e personalizar. Pode levar várias semanas em um único projeto.
Avançar pela compreensão é mais útil do que cumprir um calendário.

Em uma sessão de 45–90 minutos:

1. Releia uma tarefa e escreva o comportamento esperado em duas frases.
2. Faça um exemplo manual e escolha um caso inválido.
3. Implemente uma parte por 20–40 minutos sem consultar a solução.
4. Execute, compare com sua previsão e registre o que descobriu.
5. Termine anotando a próxima tarefa pequena. Não deixe apenas “continuar projeto”.

## Prática ativa

Antes de rodar, preveja a saída. Troque um valor e explique o que deveria mudar.
Desenhe a lista antes e depois de remover um item. Escreva testes com exemplos
diferentes dos tutoriais. Feche a solução e reconstrua uma função de memória,
entendendo cada linha. Explique em voz alta por que seu `return` está naquela posição.

## Quando travar

Reduza o problema: um cadastro que não funciona pode virar uma função que recebe
um nome e devolve um dicionário. Use `print(type(valor), repr(valor))` para observar
tipos e espaços. Leia o traceback de baixo para cima e encontre o primeiro arquivo
seu citado. Não modifique cinco coisas ao mesmo tempo.

As dicas possuem três camadas: pergunta orientadora, estrutura sugerida e indicação
de ferramenta. Abra uma camada, feche o arquivo e tente novamente. Depois de uma
tentativa registrada, consulte apenas a função correspondente na solução. Se ainda
precisar de ajuda, abra uma issue com passos, saída esperada e saída observada.

## Como usar os testes

Os testes da referência importam o pacote de `solucao/`. Eles usam pastas temporárias
e não devem tocar seus arquivos reais. Rodar esses testes não valida automaticamente
seu código inicial: primeiro implemente funções equivalentes, depois mude o caminho
de importação no seu fork ou crie seus próprios testes. Os tutoriais mostram casos
de comportamento para começar sem reproduzir a arquitetura inteira.

## Tornando o projeto autoral

Escolha uma necessidade sua: alimentos de uma república, propostas de revisão de
textos ou candidaturas de estágio. Altere uma regra, acrescente testes e documente
a decisão. Mude o nome e a interface com propósito, não apenas as cores ou palavras.
Mostre uma execução e explique limitações no seu README. Credite a base MacacoDev.

Estudar a referência é aprender uma decisão. Copiar sem compreender não demonstra
autonomia. Uma adaptação autoral tem escolhas que você consegue justificar, testes
que você escreveu e mudanças que consegue explicar numa entrevista.

## Ferramentas da referência que podem ser novas

**Pacote e importação relativa.** Uma pasta com `__init__.py` reúne módulos num
pacote. Em `terminal.py`, `from .dominio import cadastrar` procura o módulo vizinho
dentro do mesmo pacote. Execute `solucao/main.py`, a entrada documentada, em vez
de executar `terminal.py` sozinho. O arquivo de entrada conecta as partes.

**`if __name__ == "__main__"`.** Esse bloco chama o programa quando o arquivo é
executado diretamente. Ao importar uma função em um teste, o menu não deve abrir.
`raise SystemExit(main())` entrega ao sistema o código retornado: zero indica
encerramento normal; um indica falha de abertura dos dados.

**`pathlib` e `argparse`.** `Path` representa caminhos sem concatenar barras
específicas de Windows ou Linux. `Path(__file__)` parte do arquivo do programa;
por isso os dados padrão não mudam conforme a pasta do terminal. `argparse` lê
opções como `--dados experimento.json` e produz a ajuda `--help`. Não é necessário
reimplementar essas bibliotecas para aprender suas aplicações.

**`deepcopy`.** Atribuir `novo = estado` não cria outro dicionário. Mesmo uma cópia
simples mantém referências para listas e dicionários internos. A referência usa
`deepcopy` para preparar um estado separado. Se a validação ou a gravação falhar,
o estado anterior continua válido. Experimente uma lista de dois dicionários para
ver a diferença; não memorize a ferramenta sem observar o problema.

**`with` e escrita por substituição.** `with` fecha arquivo/conexão ao sair do bloco,
mesmo se houver exceção. `arquivos.py` primeiro escreve um temporário no mesmo
diretório, descarrega o buffer e fecha o arquivo; só depois substitui o destino.
O bloco `finally` limpa o temporário. Isso reduz o risco de arquivo parcialmente
gravado durante uma falha da aplicação; não substitui backups nem cria suporte
a duas instâncias editando o mesmo JSON.

**`unittest`, `assert` e mock.** Um teste chama uma função com entrada conhecida e
compara a saída com `assertEqual`, ou espera uma exceção com `assertRaises`.
`TemporaryDirectory` separa dados de teste dos seus dados reais. Um mock substitui
somente uma dependência, como rede ou teclado, por um comportamento controlado.
No BuscaCEP, a interpretação do endereço continua real; só o HTTP é simulado.

**Expressões regulares.** `re.fullmatch` pergunta se a string inteira segue um
padrão. No CEP, `[0-9]{5}-?[0-9]{3}` aceita cinco dígitos, um hífen opcional e três
dígitos. Primeiro entenda e teste essas posições com strings; depois estude a
notação. Não use padrões enormes onde condições simples forem mais claras.
