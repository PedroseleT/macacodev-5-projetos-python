# Desafios

## Fácil · observações
Descrição: incluir observações opcionais nas candidaturas. Objetivo: ampliar o modelo
sem quebrar registros antigos. Requisitos: limite de tamanho, edição e campo vazio
para registros antigos. Conclusão: carregar JSON antigo continua funcionando e
editar observação preserva demais campos. Dicas: comece pelo valor padrão; teste
ausência da chave; documente mudança de formato se necessário.

## Médio · filtro por período
Descrição: consultar candidaturas entre duas datas. Objetivo: comparar datas.
Requisitos: intervalo inclusivo, rejeitar início posterior ao fim e tratar Interesse
sem data. Conclusão: testes cobrem ambas as bordas e intervalo sem resultados.
Dicas: converta entradas antes de filtrar; defina o comportamento de data ausente.

## Avançado · candidaturas sem atualização
Descrição: destacar registros sem mudança há determinado número de dias.
Objetivo: analisar estado temporal sem inventar eventos. Requisitos: relógio
substituível nos testes, prazo válido e política para estados finais. Conclusão:
um registro recente não aparece e um antigo aparece no limite definido. Dicas:
use atualizada_em; não confunda data da candidatura com última alteração; documente
que ausência de atualização não significa rejeição da empresa.
