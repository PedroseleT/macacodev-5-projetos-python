# Git e GitHub sem pular etapas

**Git** registra versões no seu computador. **GitHub** hospeda repositórios e facilita
colaboração. Baixar ZIP permite estudar, mas não traz o histórico Git. Um **fork** é
uma cópia no seu GitHub; um **clone** baixa um repositório com seu histórico.

## Instalar e identificar seus commits

Instale pelo [site do Git](https://git-scm.com/downloads) e abra um novo terminal.
No seu computador, substitua os textos abaixo por sua identificação. Se não quiser
expor seu e-mail, use o endereço noreply fornecido em Settings → Emails no GitHub.

```sh
git --version
git config --global user.name "Seu nome público"
git config --global user.email "SEU_EMAIL_NOREPLY_DO_GITHUB"
```

## Estudar sem publicar mudanças

```sh
git clone https://github.com/PedroseleT/macacodev-5-projetos-python.git
cd macacodev-5-projetos-python
git status
git log --oneline -5
```

`status` mostra alterações locais. `log` mostra versões anteriores. Um **commit**
registra um conjunto de alterações com uma mensagem explicando a intenção.

## Adaptar com um fork

No GitHub, clique **Fork → Create fork**. Copie a URL HTTPS do SEU fork e execute:

```sh
git clone URL_DO_SEU_FORK
cd macacodev-5-projetos-python
git switch -c melhoria-pesquisa-alimentos
```

Faça uma alteração pequena e execute os testes. Antes de registrar:

```sh
git diff
git status --short
git add 01-desperdicio-zero/solucao 01-desperdicio-zero/testes
git diff --cached
git commit -m "Adiciona pesquisa de alimentos por nome"
git push -u origin melhoria-pesquisa-alimentos
```

`add` prepara arquivos; `commit` cria a versão local; `push` envia ao seu GitHub.
O exemplo usa caminhos que existem. Escolha somente os arquivos da sua mudança.
O GitHub pode abrir autenticação no navegador; não coloque senha/token em arquivos,
comandos compartilhados ou URL do remoto. Não use a senha da conta como token.

## Publicar um projeto independente

Crie um repositório vazio no seu GitHub, sem inicializar README. Copie apenas o
projeto que adaptou para uma pasta nova, preservando a licença MIT e os créditos.
Não copie `dados/`, `__pycache__/`, senhas ou informações reais de clientes.
Na pasta nova, crie seu README e um `.gitignore` antes de executar:

```sh
git init
git branch -M main
git add .
git diff --cached
git commit -m "Publica minha adaptação do projeto MacacoDev"
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Os valores em maiúsculas são marcadores: substitua por URLs reais da sua conta.
Se já existe um remoto `origin`, confira `git remote -v` antes de alterar qualquer
coisa. Nunca force um push para resolver um erro sem entender o que será substituído.

## Contribuir de volta

Abra um Pull Request do seu fork para este projeto e explique problema, mudança e
testes executados. Confira [COMO-CONTRIBUIR.md](COMO-CONTRIBUIR.md).
Para atualizar sua cópia local, salve ou registre suas mudanças antes de `git pull`.
Uma issue descreve uma dúvida/defeito; um Pull Request propõe alteração de arquivos.
