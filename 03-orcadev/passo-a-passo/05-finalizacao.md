# 5. Evolua sozinho

Faça uma proposta com dois serviços e um desconto. Feche o aplicativo, abra de
novo e exporte o mesmo ID. Compare subtotal e total manualmente. Não basta existir
um TXT: as regras, o cliente e os centavos precisam estar corretos.

Explique por que preços são strings no JSON e Decimal nas operações. Depois
explique por que guardar um total solto pode produzir inconsistência. Se essas
respostas ainda dependerem da referência, faça mais um exemplo pequeno.

Escolha um desafio de [desafios.md](../desafios.md), escreva a regra e crie um teste
antes da interface. Desconto percentual exige decidir quando arredondar; validade
exige decidir se uma proposta vencida pode ser consultada. As decisões devem estar
escritas, não escondidas numa condição.

Para seu portfólio, adapte a um serviço que você conhece sem usar dados de cliente
real. Mostre um orçamento demonstrativo e explique que a ferramenta não substitui
um sistema fiscal. Registre créditos e limitações. Consulte [dicas.md](../dicas.md)
se precisar de uma direção sem ver a resposta completa.

Confira o [checklist](../checklist.md), rode os testes e faça um commit descritivo.
O próximo projeto troca cálculos financeiros por uma política que muda a cada
chamada: [Fila Justa](../../04-fila-justa/README.md).
