# Dicas em camadas

Pare depois de uma camada e tente novamente.

<details><summary>1 · Qual estrutura representa o problema?</summary>
Um alimento tem vários campos relacionados. Vários alimentos formam uma coleção.
Desenhe dois registros e descubra por que uma lista de nomes não basta.
</details>

<details><summary>2 · Como separar cadastro e teclado?</summary>
Receba parâmetros em uma função e devolva o novo registro. Deixe `input` no menu.
Teste a função com valores escritos diretamente no código antes de ligar a interface.
</details>

<details><summary>3 · Como calcular o alerta?</summary>
Converta para `date`, subtraia a data de referência e consulte `.days`.
Teste negativo, zero, três e quatro. Faça isso antes de filtrar a lista inteira.
</details>

<details><summary>Persistência · não sei por onde começar</summary>
Faça ida e volta com `json.dumps` e `json.loads` na memória. Depois use
`Path.write_text` e `Path.read_text` num arquivo temporário. A referência acrescenta
escrita por substituição para preservar o destino se a gravação falhar.
</details>
