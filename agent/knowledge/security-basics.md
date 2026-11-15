# Fundamentos de segurança para análise de vulnerabilidades

Este material complementa a skill `vulnerability-analysis`.

## Conceitos

- **Ativo:** sistema, serviço, equipamento ou informação que precisa de proteção.
- **Vulnerabilidade:** fraqueza em código, configuração, processo ou controle que pode ser explorada.
- **Ameaça:** agente, evento ou condição que pode causar dano.
- **Risco:** possibilidade de uma ameaça explorar uma vulnerabilidade e gerar um impacto. Depende do contexto, não apenas da existência da falha.
- **Evidência:** informação observável que sustenta uma conclusão. Uma suspeita não é uma confirmação.

## Tríade CIA

| Pilar | O que significa | Exemplo |
| --- | --- | --- |
| Confidencialidade | Impedir divulgação não autorizada | Exposição de dados de usuários |
| Integridade | Impedir alteração não autorizada | Modificação de registros no banco |
| Disponibilidade | Manter serviços acessíveis | Interrupção de um sistema crítico |

Um mesmo problema pode afetar mais de um pilar.

## Avaliação de risco

Antes de classificar, verifique a exposição, os privilégios necessários, a facilidade de exploração, os controles existentes, os dados envolvidos e a importância do serviço para a operação.

- **Impacto:** consequência caso o cenário se concretize.
- **Probabilidade:** quão plausível é que ocorra, dadas as condições reais.
- **Severidade:** classificação resultante da avaliação, com justificativa e limitações.

Não use a matriz didática da skill como se fosse CVSS. Para informar uma pontuação CVSS real, utilize a especificação e as métricas adequadas; não invente números.

Em infraestrutura corporativa, uma correção também precisa considerar disponibilidade, homologação, janela de mudança, reversão e responsável pela aprovação.

## SQL Injection

Ocorre quando valores fornecidos ao programa são concatenados ao comando SQL e acabam sendo interpretados como parte da instrução. A classificação conhecida é **CWE-89**.

Para corrigir, use **consultas parametrizadas** e privilégios mínimos. Validar entrada pode complementar a segurança, mas não substitui parametrização. Em aplicações reais, senhas devem ser armazenadas com hashing apropriado; os exemplos deste projeto usam dados fictícios para isolar o conceito.

**MITRE ATT&CK** descreve comportamentos de adversários, e **CWE** classifica fraquezas. A técnica ATT&CK **T1190 — Exploit Public-Facing Application** só deve ser relacionada quando o cenário envolver exploração de uma aplicação realmente exposta publicamente. SQL Injection, isoladamente, não comprova T1190.

## Cuidados em análise de servidores

Um serviço aberto não é automaticamente uma vulnerabilidade. Um executável com SUID também não significa, sozinho, que existe escalação de privilégios. Confirme versões, configuração, exposição, pré-requisitos e evidências.

Trabalhe somente com autorização; prefira verificações de baixo impacto. Nunca publique credenciais, tokens, dados pessoais ou detalhes internos desnecessários em relatórios públicos.

## Fontes

- [CWE-89 — SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK — T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [FIRST — CVSS](https://www.first.org/cvss/)
