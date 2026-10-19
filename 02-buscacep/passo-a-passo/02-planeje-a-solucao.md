# 2. Planeje a solução

Desenhe quatro partes: normalização do CEP, transporte HTTP, interpretação da
resposta e histórico. O menu apenas combina essas partes. Assim, um teste consegue
validar um JSON sem tocar na rede.

Entrada: string como “01001-000”. Saída normalizada: “01001000”. Não converta CEP
em inteiro: o zero inicial faz parte do identificador. Remover todos os caracteres
não numéricos também pode esconder um erro como “abc01001000”. Nesta versão, aceitamos
apenas oito dígitos, um hífen opcional na posição certa e espaços externos.

## Contrato das funções

Planeje `normalizar_cep(cep)`, `interpretar_resposta(dados)` e `consultar(cep)`.
A primeira devolve texto validado; a segunda devolve um endereço com campos
conhecidos; a terceira coordena rede e validação. Uma exceção significa que a
operação não produziu um endereço válido.

```text
validar CEP localmente
montar URL apenas com os oito dígitos
abrir conexão com tempo limite
ler corpo e converter JSON
se erro do serviço: informar CEP não encontrado
validar campos e correspondência do CEP
mostrar endereço
registrar e salvar histórico
```

O histórico será uma lista de consultas, cada uma com endereço e data/hora. Repetir
o mesmo CEP gera outra consulta: estamos registrando ações, não mantendo um cadastro
único de ruas. Documentar isso evita uma deduplicação acidental.

## Pense no teste antes da rede

Escreva um dicionário de referência com `cep`, `logradouro`, `bairro`, `localidade`
e `uf`. Qual campo pode vir vazio? Um CEP geral de município pode não ter rua ou
bairro; isso não torna o endereço automaticamente inválido. Já cidade ausente ou
um array no lugar do dicionário são respostas inesperadas.

Prepare uma lista de exemplos e siga para [implementar por partes](03-primeira-implementacao.md).
