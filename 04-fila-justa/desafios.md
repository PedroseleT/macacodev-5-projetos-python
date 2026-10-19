# Desafios

## Fácil · estatística por categoria
Descrição: mostrar percentual de concluídos comuns e prioritários. Objetivo:
praticar divisão e contagens. Requisitos: usar somente concluídos; tratar zero.
Conclusão: zero atendimentos não causa divisão por zero e percentuais somam 100
quando há atendimentos. Dicas: conte antes; calcule depois; arredonde só na exibição.

## Médio · política configurável
Descrição: permitir proporção 1:1 ou 2:1 ao iniciar. Objetivo: parametrizar regras.
Requisitos: manter FIFO, salvar a configuração e rejeitar proporções inválidas.
Conclusão: testes reproduzem duas sequências diferentes com os mesmos registros.
Dicas: isole a escolha da categoria; não duplique a função inteira.

## Avançado · dois guichês
Descrição: permitir duas senhas em atendimento. Objetivo: ampliar o modelo de estado.
Requisitos: guichês identificados, conclusão por guichê e nenhum ID duplicado.
Conclusão: reiniciar preserva ambos os atendimentos e a ordem da fila. Dicas:
troque a vaga única por um dicionário de guichês; escreva invariantes antes de migrar.
