# 3. OrçaDev 💼

**Quanto custa esse serviço? Vamos montar a conta e deixar tudo organizado.**

Imagine que você vai fazer dois serviços para alguém. Precisa anotar o que será
feito, quanto custa cada parte e se vai dar desconto. O OrçaDev junta essas
informações em um orçamento que você pode salvar e consultar depois.

### [Começar: pensar em um orçamento simples →](passo-a-passo/01-entenda-o-problema.md)

## Um exemplo do que vamos criar

```text
Cliente: Cliente de demonstração

Revisão de página: 2 unidades de R$ 12,50 = R$ 25,00
Desconto: R$ 5,00
Total: R$ 20,00
```

Você poderá cadastrar clientes, adicionar serviços, calcular os valores e guardar
vários orçamentos. Também vamos gerar um arquivo de texto com a proposta.
É um exercício de organização; não emite nota fiscal nem substitui um contrato.

## O que tem de novo?

Vamos pensar em como as informações se conectam: cada orçamento pertence a um
cliente e tem seus próprios serviços. E vamos cuidar dos centavos com uma
ferramenta do Python chamada `Decimal`, explicada quando chegar a hora da conta.

Você não precisa ser freelancer para acompanhar. Use nomes genéricos e invente
um serviço simples, como revisão de uma página. O importante é entender a conta.

## Vamos por partes

1. [Entenda o pedido do cliente](passo-a-passo/01-entenda-o-problema.md)
2. [Organize o que precisa guardar](passo-a-passo/02-planeje-a-solucao.md)
3. [Monte o orçamento aos poucos](passo-a-passo/03-primeira-implementacao.md)
4. [Resolva os problemas que aparecerem](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Adapte para uma ideia sua](passo-a-passo/05-finalizacao.md)

[Precisa de uma dica?](dicas.md) · [Ideias para continuar](desafios.md)
· [O que já consegui fazer?](checklist.md)

<details><summary>Quero experimentar a versão pronta</summary>

No terminal, na pasta principal dos cinco projetos:

```sh
python 03-orcadev/solucao/main.py
```

Cadastre um cliente com a opção `1`. Depois escolha `2` para montar o orçamento.
Digite preços como `12,50` ou `12.50`, sem `R$` e sem separador de milhar.
A quantidade de cada serviço é inteira: 1, 2, 3... O desconto é um valor em reais,
não uma porcentagem. Ele não pode ser maior que a soma dos serviços.

Use `3` para listar as propostas, `4` para abrir e salvar novamente uma delas
como texto, e `0` para sair.

</details>

<details><summary>Onde ficam meus orçamentos?</summary>

Os cadastros ficam em `dados/orcamentos.json`, dentro deste projeto. As propostas
em texto ficam na pasta `dados/orcamentos`, com nomes como `orcamento-0001.txt`.
Você pode abrir o TXT em um editor de texto.

Se o cadastro for salvo, mas o TXT não puder ser criado, o programa avisa.
Não precisa cadastrar tudo de novo: use a opção `4` para tentar gerar o texto.
Faça backup com o programa fechado e guarde uma cópia antes de corrigir arquivos
com problema. Use uma janela por vez e não publique dados reais de clientes.

</details>

[Voltar ao início](../README.md) · [Como pedir ajuda](../COMO-CONTRIBUIR.md)
