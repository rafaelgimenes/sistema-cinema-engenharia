# 🎬 Sistema de Rede de Cinemas

Projeto enxuto para a aula de Engenharia de Software.

## 🚀 Requisitos e Regras
- **RF01:** Consultar filmes em cartaz e detalhes das sessões.
- **RF02:** Realizar a compra de ingressos (Tickets) pelo espectador.
- **RF03:** Manter cadastros de filmes, salas e cinemas (Funcionário).
- **RF04:** Gerenciar agendamento de sessões e horários (Funcionário).
- **RF05:** Gerar relatórios de público e faturamento (Administrador).
- **RN01:** Intervalo de 20min entre sessões na mesma sala para limpeza.
- **RN02:** Respeitar capacidade máxima da sala (bloqueio de venda).
- **RN03:** Verificação de classificação indicativa conforme idade do espectador.
- **RN04:** Proibição de choque de horários (duas sessões na mesma sala).
- **RN05:** Registro obrigatório de logs de vendas para auditoria diária.

## 📊 Diagramas do Sistema

### 1. Casos de Uso
![Casos de Uso](./docs/diagramas/casos_de_uso.png)

### 2. Classes de Domínio
![Classes de Domínio](./docs/diagramas/casos_de_dominio.png)

### 3. Diagrama de Sequência (Arquitetura MVC)
![Sequência](./docs/diagramas/sequencia_de_consulta.png)

## 🛠️ Implementação
O sistema utiliza **Python** com **SQLite** seguindo as camadas:
`View -> Controller -> Service -> Repository`
