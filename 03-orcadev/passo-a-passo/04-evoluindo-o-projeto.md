# 4. Aprenda com os erros

## O total tem casas inesperadas

Observe `print(type(preco), repr(preco))`. Se for float, a aproximação entrou antes
do Decimal. Construa a partir de string. Quantizar para centavos define escala e
arredondamento; nesta versão, entradas com frações de centavo são rejeitadas.
Não deixe a formatação bonita esconder uma conta feita com o tipo errado.

## “TypeError: Object of type Decimal is not JSON serializable”

JSON não conhece Decimal. Seu preço pode ser `"12.50"` no disco e Decimal durante
a conta. Faça uma ida e volta isolada e compare o valor recuperado. Converter para
float para “resolver o JSON” reintroduz o problema de precisão.

## O desconto passa e o total fica negativo

A checagem foi esquecida ou colocada só no menu. Chame a função de cálculo
diretamente com desconto maior que subtotal. Se ela aceitar, o erro está na regra.
Adicione um teste que espere `ValueError`; depois corrija a função, não apenas a tela.

## O TXT falhou, mas o orçamento aparece

JSON e TXT são operações diferentes. O primeiro preserva o cadastro e o segundo é
uma apresentação regenerável. Confira a mensagem antes de criar outra proposta,
evitando duplicatas. Tente exportar o mesmo ID novamente pela opção 4.

## Proposta associada ao cliente errado

Confundir ID com índice é um erro comum. Mostre ambos ao depurar e procure o registro
pelo campo `id`. Não use diretamente `clientes[id]`: listas começam em zero e podem
mudar. Teste um ID ausente e confirme que nenhum orçamento parcial foi salvo.

Leia o traceback até a primeira linha sua. Crie um exemplo mínimo para cada erro,
registre o teste e siga para [personalizar](05-finalizacao.md).
