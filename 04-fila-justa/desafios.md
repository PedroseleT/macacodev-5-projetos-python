# Ideias para o próximo atendimento

Escolha uma melhoria por vez. Continue tratando este projeto como exercício,
sem prometer cumprir todas as regras de um estabelecimento real.

## Para começar: porcentagem por categoria

Mostre qual parte dos atendimentos concluídos foi comum e qual foi prioritária.
A ideia é praticar contagem e divisão.

**Está pronto quando:** dois comuns e dois prioritários mostram 50% para cada
categoria, e nenhum atendimento concluído não provoca divisão por zero.

<details><summary>Uma pista</summary>
Conte os concluídos antes de dividir. Se o total for zero, mostre que ainda
não há atendimentos para calcular a porcentagem.
</details>

## Um passo além: escolher a alternância

Permita escolher entre uma prioritária e uma comum ou duas prioritárias e
uma comum. Mantenha a ordem de chegada dentro de cada categoria.

**Está pronto quando:** a mesma sequência de chegadas pode produzir as duas
ordens previstas e a escolha continua salva depois de reabrir.

<details><summary>Uma pista</summary>
Desenhe as duas sequências antes de mexer no código. Troque o limite usado
na decisão, sem copiar a função inteira para cada opção.
</details>

## Um desafio maior: dois guichês

Permita dois atendimentos ao mesmo tempo, cada um num guichê identificado.

**Está pronto quando:** uma senha nunca aparece em dois lugares, concluir um
guichê não afeta o outro e ambos são recuperados ao abrir novamente.

<details><summary>Uma pista</summary>
Em vez de uma única senha ativa, pense num dicionário com uma entrada por guichê.
Faça uma cópia dos dados antes de mudar a forma de salvar.
</details>

[Voltar à última etapa](passo-a-passo/05-finalizacao.md)
