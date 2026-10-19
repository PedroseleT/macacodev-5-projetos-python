# 5. Radar de Vagas Dev 🚀

**Você mandou currículo para qual empresa mesmo? Bora organizar isso.**

No desafio final, vamos criar um lugar para anotar as vagas que te interessam,
as candidaturas enviadas e as etapas em que cada uma está. Assim você não
precisa lembrar tudo de cabeça ou procurar entre várias anotações.

### [Começar: pensar no seu acompanhamento de vagas →](passo-a-passo/01-entenda-o-problema.md)

## O que vai aparecer na tela?

```text
Empresa de demonstração | Estágio em desenvolvimento
Situação: Candidatura enviada
Data: 18/10/2026
Link: https://example.org/vaga
```

Esse link é só um exemplo, não uma oportunidade anunciada.
Você vai cadastrar as vagas por conta própria; o programa não procura vagas
na internet nem envia currículos.

## O que vamos juntar neste projeto?

Cadastrar, listar, corrigir e excluir informações. Procurar uma empresa pelo
nome e ver somente as candidaturas em uma situação, como Entrevista.
Depois, salvar uma tabela que pode ser aberta em um programa de planilhas.

Vamos usar bastante do que apareceu nos quatro projetos anteriores.
Se uma parte parecer grande demais, volte a uma tarefa menor e faça só ela.

## Acompanhe por aqui

1. [Entenda o que vale anotar](passo-a-passo/01-entenda-o-problema.md)
2. [Organize as informações](passo-a-passo/02-planeje-a-solucao.md)
3. [Monte o programa em partes](passo-a-passo/03-primeira-implementacao.md)
4. [Resolva os erros mais comuns](passo-a-passo/04-evoluindo-o-projeto.md)
5. [Termine com uma versão sua](passo-a-passo/05-finalizacao.md)

[Precisa de uma dica?](dicas.md) · [Ideias para continuar](desafios.md)
· [O que já consegui fazer?](checklist.md)

<details><summary>Quero abrir a versão pronta</summary>

No terminal, na pasta principal dos cinco projetos:

```sh
python 05-radar-de-vagas/solucao/main.py
```

Use `1` para cadastrar, `2` para listar, `3` para escolher uma situação,
`4` para pesquisar empresa, `5` para atualizar e `6` para excluir.
A opção `7` mostra contagens, `8` salva a tabela e `0` sai.

As situações são Interesse, Candidatura enviada, Entrevista, Teste técnico,
Proposta, Aprovado e Rejeitado. Você escolhe a situação manualmente.
Em Interesse, a data de candidatura pode ficar vazia: você ainda não enviou.
Nas demais situações, informe uma data real como `18/10/2026`.

O link deve começar com `http://` ou `https://`. Aceitar o formato do link
não significa que o programa sabe se a vaga ainda está aberta.

</details>

<details><summary>Onde ficam os registros e a tabela?</summary>

Os registros ficam em `dados/candidaturas.json`, dentro deste projeto.
A tabela fica em `dados/exportacoes/candidaturas.csv`. CSV é um formato de
texto que programas de planilha conseguem abrir. Uma nova exportação substitui
a tabela anterior; os cadastros continuam no JSON.

Se os acentos aparecerem errados no Excel, use a opção de importar texto/CSV,
escolha a codificação UTF-8 e o separador vírgula. O cadastro original não muda.

Faça backup com o programa fechado. Se o arquivo tiver problema, preserve
uma cópia antes de tentar corrigir ou recuperar um backup. Use uma janela por
vez e não publique currículo, contatos ou links privados junto do código.

</details>

[Voltar ao início](../README.md) · [Como pedir ajuda](../COMO-CONTRIBUIR.md)
