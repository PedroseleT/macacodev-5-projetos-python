# 2. Planeje a solução

Separe três entidades: cliente, serviço dentro da proposta e orçamento. Cliente
tem ID e nome. Serviço tem descrição, quantidade e preço unitário. Orçamento tem
ID, cliente, data, serviços e desconto.

Não precisamos de um banco externo. Uma lista de clientes e outra de propostas
resolvem este porte. A relação por `cliente_id` ensina a conectar registros sem
copiar o cadastro todo. Antes de salvar, confirme que o cliente existe.

## Dinheiro exige uma escolha explícita

`float` representa frações em binário; centavos podem não ter representação exata.
Com `Decimal`, o valor é construído a partir do texto:

```python
from decimal import Decimal

preco = Decimal("0.10")
print(preco * 3)  # 0.30
```

Não use `Decimal(0.1)`: o float já passou pela aproximação. A referência aceita
duas casas nos valores de entrada, usa centavos e rejeita mais casas em vez de
arredondar silenciosamente. Consulte a [documentação do Decimal](https://docs.python.org/3.11/library/decimal.html).

## Planeje as funções

`criar_item` valida um serviço. `calcular_totais` soma quantidade vezes preço e
subtrai o desconto. `criar_orcamento` liga cliente e serviços. `formatar_orcamento`
devolve uma string, sem imprimir nem abrir arquivo. O menu decide quando exibir
e quando escrever essa string.

```text
cadastrar ou escolher cliente
receber serviços validados
calcular totais e conferir desconto
criar proposta com ID
salvar JSON
formatar e exportar TXT
```

Decimal não é serializável diretamente pelo JSON padrão. Guarde `"12.50"` e
reconstrua Decimal ao calcular. Não guarde um total independente que pode divergir
dos itens. Desenhe seu JSON e siga para [construir](03-primeira-implementacao.md).
