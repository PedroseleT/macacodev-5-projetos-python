# 02 · BuscaCEP Inteligente 📍

**Iniciante a intermediário · consulte um endereço sem digitar cada campo.**

O programa recebe CEP com ou sem hífen, consulta o ViaCEP e mostra logradouro,
bairro, cidade e estado. Consultas válidas ficam num histórico local, inclusive
consultas repetidas. O histórico pode ser lido offline.

```text
1 Consultar CEP | 2 Histórico | 0 Sair
Escolha: 1
CEP: 01001-000
CEP: 01001-000
Logradouro: Praça da Sé
Bairro: Sé
Cidade: São Paulo | Estado: SP
Consulta salva no histórico.
```

Exemplo de endereço público de referência do [ViaCEP](https://viacep.com.br/), não
dado de uma pessoa. Uma resposta pode mudar com a base do serviço.

## Funcionalidades e conceitos

Validação local de oito dígitos ASCII, consulta HTTPS com timeout de 10 segundos,
tratamento de CEP inexistente, HTTP inesperado, conexão, JSON inválido e resposta
incompleta. Respostas não correspondentes ao CEP solicitado são rejeitadas. Rua e
bairro vazios são permitidos para CEPs genéricos de município.

Você pratica strings, funções, módulos, exceções, APIs, JSON, `urllib.request` e
persistência. Precisa entender funções e arquivos do projeto anterior. API,
requisição e resposta são explicadas no tutorial, antes da chamada de rede.

## Instalação e execução

Python 3.11+; nenhuma dependência para instalar. Na raiz:

```sh
python 02-buscacep/codigo-inicial/main.py
python 02-buscacep/solucao/main.py
python 02-buscacep/solucao/main.py --dados 02-buscacep/dados/experimento.json
```

Só consultas novas exigem internet. O programa não coleta pessoas, não usa chaves
de API e não consulta bases em massa. Respeite a [orientação do ViaCEP](https://viacep.com.br/).

## Estrutura e persistência

```text
codigo-inicial/main.py, tarefas.py
solucao/main.py
solucao/buscacep/servico.py        validação e HTTP
solucao/buscacep/dominio.py        histórico de consultas válidas
solucao/buscacep/arquivos.py       JSON e escrita por substituição
solucao/buscacep/terminal.py       menu
testes/test_buscacep.py
passo-a-passo/                    cinco tutoriais
```

Padrão: `02-buscacep/dados/historico.json`, calculado a partir da localização do
programa, não do diretório atual. Criado na primeira consulta salva. Data/hora de
consulta usa ISO com fuso UTC; o endereço conserva o formato retornado pela API.
Arquivo ausente inicia histórico vazio. Falha de consulta não cria registro.

Arquivo corrompido, versão desconhecida ou estrutura inválida impedem abertura:
o original é preservado. Feche o programa, faça cópia e restaure um backup ou
corrija o JSON. Para zerar por decisão sua, mova o arquivo para outro lugar.
Uma falha de gravação é informada; o endereço consultado não deve ser confundido
com histórico salvo. Não execute duas instâncias sobre o mesmo JSON.

## Testes offline

```sh
cd 02-buscacep
python -m unittest discover -s testes -v
```

As respostas HTTP são simuladas, incluindo erro 503, timeout, CEP inexistente,
UTF-8 inválido, JSON inesperado e resposta muito grande. Não há chamadas reais de
rede nos testes. Sua implementação pode receber uma função de consulta simulada;
veja o tutorial antes de estudar o uso de mocks na referência.

## Trilha

1. [Entenda o problema](passo-a-passo/01-entenda-o-problema.md)
2. [Planeje](passo-a-passo/02-planeje-a-solucao.md)
3. [Construa](passo-a-passo/03-primeira-implementacao.md)
4. [Depure](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Evolua](passo-a-passo/05-finalizacao.md)

[Desafios](desafios.md) · [Dicas](dicas.md) · [Checklist](checklist.md) · [Voltar](../README.md)
