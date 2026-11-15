# 🤖 DIO Agent — análise de vulnerabilidades

> Minha evolução do [DIO Agent original](https://github.com/digitalinnovationone/dio-agent) para o desafio da DIO.

## O que eu acrescentei

Escolhi especializar o agente em **análise de vulnerabilidades**, pensando no que venho estudando em Segurança da Informação e no trabalho com infraestrutura. Antes de sair sugerindo comandos ou classificando tudo como crítico, ele precisa entender o ambiente, procurar evidências, avaliar o risco e só depois propor a correção.

A melhoria que escolhi foi **padronizar o parecer em contexto, evidência, causa raiz, impacto, probabilidade, severidade, correção e validação**. Também acrescentei um exemplo local de SQL Injection para comparar um login vulnerável com a versão corrigida.

### Arquivos que criei ou alterei

| Arquivo | Alteração |
| --- | --- |
| [SKILL.md](skills/vulnerability-analysis/SKILL.md) | Etapas que o agente deve seguir na análise |
| [README da skill](skills/vulnerability-analysis/README.md) | Objetivo e exemplos de uso |
| [security-basics.md](agent/knowledge/security-basics.md) | Fundamentos de segurança e classificação de riscos |
| [persona.md](agent/persona.md) | Comportamento do mentor ao tratar vulnerabilidades |
| [AGENTS.md](AGENTS.md) | Registro da skill e do conhecimento |
| [app.py](examples/sql-injection/app.py) | Login propositalmente vulnerável no SQLite em memória |
| [app_fixed.py](examples/sql-injection/app_fixed.py) | Correção com consulta parametrizada |
| [test_login.py](examples/sql-injection/test_login.py) | Validação automatizada das duas versões |

### Como executar no Hermes

Depois de instalar o [Hermes](https://hermes-agent.nousresearch.com/docs) conforme a documentação oficial, abra um terminal **na pasta do projeto**:

```bash
git clone https://github.com/LuizPaivaa/dio-agent-cybersecurity.git
cd dio-agent-cybersecurity
hermes
```

Exemplo de conversa:

> Analise o arquivo `examples/sql-injection/app.py` como especialista em AppSec. Avalie a causa raiz, o impacto e a correção em `app_fixed.py`. Não presuma que essa aplicação é pública e não invente resultados.

Para executar os testes de código em Python 3, sem bibliotecas externas:

```bash
python -m unittest discover -s examples/sql-injection -p "test_*.py" -v
```

O SQLite usa apenas memória e credenciais fictícias. Os testes verificam o comportamento vulnerável e a rejeição da entrada manipulada após a correção.

**Validação do exemplo:** reproduzi os arquivos do laboratório em Python 3 e executei os três testes: login válido, senha incorreta e tentativa de SQL Injection. Todos passaram. O teste de injeção confirmou o comportamento inseguro no exemplo original e a rejeição na versão corrigida.

**Limite:** isso valida apenas o código Python, não a skill no Hermes. Uma conversa real no harness ainda precisa ser feita; não incluí prints ou resultados dessa etapa sem executá-la.

---


> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/LuizPaivaa/dio-agent-cybersecurity.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent-cybersecurity`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa falhas em código ou infraestrutura e orienta correções | "Quero revisar este login e entender o risco." |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           O que o agente sabe sobre a DIO
├── skills/                  Uma pasta por skill, incluindo vulnerability-analysis
├── examples/sql-injection/  Código vulnerável, correção e testes
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
