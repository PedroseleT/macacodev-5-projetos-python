# 2. Planeje a solução

Entradas: nome, quantidade, validade e opção de menu. Saídas: registro salvo,
listagem, classificação da data ou mensagem de erro. Comece separando a regra de
negócio da leitura do teclado: uma função que recebe valores é fácil de testar.

## Modele um registro

```python
alimento = {"id": 1, "nome": "Banana", "quantidade": 6, "validade": "2026-10-20"}
```

O dicionário reúne informações de um alimento; uma lista reúne vários alimentos.
O ID é identidade, não posição: remover o primeiro item não deve mudar o ID dos
demais. Guarde um `proximo_id` e incremente a cada cadastro.

Datas serão pedidas em DD/MM/AAAA e guardadas em AAAA-MM-DD, formato ISO. A conversão
tem responsabilidade própria: `data_de_entrada(texto)`. Para quantidade, planeje
`quantidade_valida(valor)`. Para classificar, `situacao(item, hoje, dias)`.
Receber `hoje` nos testes evita depender da data real do computador.

## Organize antes de implementar

```text
carregar estado ou iniciar lista vazia
enquanto opção não for sair:
    receber opção
    se cadastrar: validar e construir novo estado
    se listar: percorrer registros
    se filtrar: comparar datas
    se remover: localizar por ID
    se houve alteração: salvar e confirmar
```

Por que salvar antes de confirmar? Se o disco negar acesso, “salvo com sucesso”
seria mentira. Na referência, funções de mudança devolvem uma cópia: o menu só
troca o estado depois de gravar. Primeiro implemente em memória; depois aprenda
esse cuidado ao adicionar persistência.

Escreva assinaturas das funções e um exemplo de retorno para cada uma. Decida se
aceitará quantidades fracionárias e como mostrará a unidade: nesta versão a unidade
pode fazer parte do nome, como “Arroz (kg)”. Quando conseguir simular um cadastro
sem teclado, passe à [construção](03-primeira-implementacao.md).
