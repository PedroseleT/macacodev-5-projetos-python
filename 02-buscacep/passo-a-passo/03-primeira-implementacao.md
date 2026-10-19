# 3. Construa por etapas

## A · valide sem internet

Objetivo: preservar os zeros e rejeitar formatos ruins. Conceito: strings e
condicionais. Tarefa: aceite “01001000” e “01001-000”; rejeite “123”, letras e espaço
interno. Esperado: sempre oito dígitos na saída válida. Teste a função diretamente,
sem `input`. Expressões regulares são opcionais na sua primeira tentativa; compare
comprimento e posições para entender a regra antes de estudar `re.fullmatch`.

## B · interprete um endereço local

Objetivo: entender JSON antes de depender de HTTP. Conceitos: dicionário e exceções.
Experimente:

```python
import json

texto = '{"localidade": "São Paulo", "uf": "SP"}'
dados = json.loads(texto)
print(dados["localidade"])
```

Tarefa: valide um endereço completo e separe o caso `{"erro": true}`. Esperado:
uma lista `[]` não é aceita como endereço. Teste campo ausente e rua vazia.

## C · faça uma consulta real controlada

Objetivo: usar uma biblioteca padrão para transporte. Conceitos: `with`, bytes e
decodificação. Estude `urllib.request.urlopen`, seu parâmetro `timeout` e a conversão
de bytes UTF-8 para texto. Tarefa: conectar o CEP validado ao parser da etapa B.
Esperado: erro de rede vira mensagem e permite outra tentativa. Não coloque a
URL recebida livremente pelo usuário: monte a URL oficial a partir do CEP validado.

## D · simule para testar

Objetivo: repetir o mesmo teste sem rede. Conceito: substituir uma dependência.
Uma função que chama a internet pode receber outra função que entrega uma resposta
controlada. Essa é a ideia por trás do `abrir` opcional e dos mocks da referência.
Tarefa: simule resposta válida e conexão indisponível. Esperado: resultados idênticos
em execuções sucessivas, mesmo com Wi-Fi desligado.

## E · mantenha histórico

Objetivo: aplicar JSON em dados já validados. Tarefa: após uma consulta bem-sucedida,
grave endereço e instante. Esperado: erro HTTP não aumenta o histórico; reiniciar
preserva consultas. A listagem do histórico não deve chamar ViaCEP. Continue para
[investigar falhas](04-evoluindo-o-projeto.md).
