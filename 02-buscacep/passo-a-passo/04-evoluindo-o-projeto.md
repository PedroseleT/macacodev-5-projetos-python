# 4. Aprenda com os erros

## “HTTPError: 400” e CEP inexistente não são iguais

Um formato inválido pode causar HTTP 400. Oito dígitos inexistentes podem produzir
um JSON com `erro`. Validar a entrada antes reduz o primeiro caso; interpretar o
corpo trata o segundo. Não transforme todo HTTPError em “CEP não existe”. Um 503
pode ser indisponibilidade do servidor.

## “URLError” ou timeout

Seu código pode estar correto e a rede falhar. Confira a mensagem, tente outra
consulta mais tarde e mantenha um tempo limite. Repetição agressiva não é solução.
Teste a mensagem com uma exceção simulada; não derrube sua própria internet para
reproduzir cada cenário.

## “JSONDecodeError”

Um servidor intermediário pode devolver HTML em vez de JSON. `json.loads` não
entende essa resposta. Ao depurar, observe uma pequena parte do corpo e o status;
não assuma que qualquer resposta HTTP é um endereço. Nunca acrescente esse erro
ao histórico como se fosse uma consulta válida.

## “KeyError: localidade”

A chave está ausente ou você confundiu o nome. Use `print(type(dados), dados)` com
um exemplo público e leia o contrato do serviço. Trocar toda chave por `.get(...,
"")` pode esconder uma resposta incompleta. Rua vazia é permitida; cidade ausente
precisa de erro explícito.

## Faça o erro virar teste

Crie uma resposta pequena que reproduza a falha. Verifique que nenhuma escrita foi
feita no histórico. Corrija a interpretação e rode todos os cenários anteriores.
O teste não deve confiar em disponibilidade, velocidade ou atualização da base
real do ViaCEP. Depois confira [os desafios](05-finalizacao.md).
