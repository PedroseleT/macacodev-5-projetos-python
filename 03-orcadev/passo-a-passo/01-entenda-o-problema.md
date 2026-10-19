# 1. Quanto ficou esse serviço?

Imagine que alguém pediu duas alterações em uma página e mais um formulário.
Você anotou um preço em uma mensagem, outro em um papel e agora precisa juntar
tudo. Dá para se perder fácil.

O OrçaDev vai organizar essa conta. Você informa o cliente, os serviços, as
quantidades e os preços. O programa calcula e prepara um orçamento em texto
para consultar depois.

## Primeiro faça a conta no papel

Pense neste exemplo:

- Duas revisões de página por R$ 12,50 cada: R$ 25,00.
- Uma configuração de formulário por R$ 5,00: R$ 5,00.
- Somando tudo: R$ 30,00.
- Tirando R$ 4,00 de desconto: R$ 26,00.

Esse valor antes do desconto é chamado de **subtotal**. Não tem segredo:
é apenas a soma dos serviços.

E se alguém informar R$ 40,00 de desconto? Nosso programa deve avisar que
o desconto não pode ser maior que o subtotal, em vez de criar um total negativo.

## O que fica para você decidir

O programa não escolhe quanto cobrar. Ele só organiza os valores informados.
Também não emite nota fiscal nem substitui um contrato de prestação de serviço.

Antes de seguir, invente dois serviços simples e escreva um orçamento à mão.
Use dados de demonstração, sem nomes ou informações de clientes reais.

Vamos transformar essa conta em pequenas funções, uma de cada vez.

[Voltar à apresentação](../README.md) · [Próximo: organizar os valores](02-planeje-a-solucao.md)
