# Dicas progressivas

<details><summary>1 · CEP não é um número para calcular</summary>
Você não vai somar dois CEPs. Guarde uma string para preservar o zero inicial.
Liste os dois formatos aceitos antes de remover o hífen.
</details>
<details><summary>2 · Como entender a resposta?</summary>
Construa um dicionário local e teste seu parser sem HTTP. Verifique tipo, erro
de CEP inexistente e campos exigidos. Não confunda rua vazia com cidade ausente.
</details>
<details><summary>3 · Como testar sem rede?</summary>
Substitua a função que abre a URL por uma função controlada. Ela pode devolver
bytes de JSON ou lançar URLError. Só o transporte deve mudar; a validação continua.
</details>
<details><summary>Histórico e cache são a mesma coisa?</summary>
Histórico registra consultas. Cache decide se pode evitar uma nova consulta.
Comece com histórico; o prazo de cache é um desafio separado.
</details>
