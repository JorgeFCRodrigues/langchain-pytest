# PyTest Agent (LangChain + Azure OpenAI)

Agente que gera automaticamente testes unitários pytest para um arquivo Python.

## Estrutura
- agent.py: CLI principal
- generator.py: Lógica do agente
- examples/functions.py: Funções de exemplo
- .env.example: Variáveis de ambiente

## Uso
1. Instale dependências:
   pip install langchain pytest openai
2. Configure suas credenciais Azure em um arquivo .env baseado em .env.example
3. Gere testes:
   python agent.py examples/functions.py
4. Rode pytest:
   pytest outputs/
