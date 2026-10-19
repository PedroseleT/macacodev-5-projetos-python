# 3. Construa por etapas

## A · cadastre e liste

Objetivo: realizar Create e Read do CRUD. Conceitos: dicionários, listas e funções.
Tarefa: crie duas oportunidades com IDs diferentes, inclusive da mesma empresa.
Esperado: listar mostra ambas, com todos os campos principais. Teste empresa vazia,
link sem protocolo e data impossível. Não acesse links durante validação: estamos
checando formato, não disponibilidade da vaga.

## B · filtre e pesquise

Objetivo: consultar subconjuntos. Conceitos: laços e comparações de strings.
Tarefa: filtre status e procure parte do nome sem distinguir maiúsculas.
Esperado: “BANANA” encontra “Banana Sistemas”; uma busca sem combinação devolve
lista vazia. Confira que a lista original continua com todos os registros.

## C · atualize com consistência

Objetivo: realizar Update. Conceitos: cópia, campos permitidos e invariantes.
Tarefa: atualize cargo e status por ID. Esperado: ID e criação permanecem iguais;
campos não enviados continuam preenchidos. Passe cargo válido e status inválido
na mesma operação: nada deve mudar. Para avançar de Interesse sem data, solicite
a data junto com a mudança de status.

## D · exclua com confirmação

Objetivo: realizar Delete sem atingir outra oportunidade. Tarefa: mostre o registro
e confirme antes de excluir. Esperado: responder algo diferente de SIM cancela;
ID inexistente informa erro. Cadastre outro depois de excluir e confirme que a
numeração não foi reutilizada.

## E · conte, salve e exporte

Objetivo: combinar persistência e apresentação. Conceitos: JSON, CSV, agregação.
Tarefa: conte por status e exporte campos para CSV com `csv.DictWriter`. Esperado:
a soma dos status é o total; uma lista vazia gera cabeçalho sem erro. Teste um nome
com vírgula e acento usando `csv.DictReader` para ler o resultado.

Saia e abra o JSON novamente antes de afirmar que concluiu. Depois vá para
[os erros frequentes](04-evoluindo-o-projeto.md).
