# Desafios

## Fácil · reapresentar do histórico
Descrição: selecionar uma consulta pelo número exibido. Objetivo: separar leitura
local de rede. Requisitos: não chamar HTTP; informar a data do registro. Conclusão:
funciona offline e rejeita índice inexistente. Dicas: enumere a lista; confira
limites antes de acessar; teste com o histórico vazio.

## Médio · exportar um endereço
Descrição: salvar um endereço escolhido em texto. Objetivo: formatar e escrever.
Requisitos: UTF-8, campos rotulados e caminho de saída informado. Conclusão: acentos
preservados e nenhuma alteração no histórico. Dicas: monte uma string antes de
escrever; teste em TemporaryDirectory.

## Avançado · cache com prazo
Descrição: reutilizar um endereço recente e permitir atualização explícita.
Objetivo: modelar validade de dados externos. Requisitos: prazo configurável,
origem local/rede visível e fallback documentado. Conclusão: testes com relógio fixo
cobrem cache recente, expirado e rede indisponível. Dicas: separe a decisão “pode
usar?” da função que consulta; consulte `dicas.md` antes de mudar tudo.
