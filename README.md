# 🐍 Projeto: Integração com LangChain em Python

Este repositório demonstra como criar **aplicações de IA
conversacional** utilizando o [LangChain](https://www.langchain.com/)
com **Python**.\
O objetivo é mostrar, de forma simples e bem documentada, como conectar
modelos de linguagem a fluxos de trabalho práticos, incluindo:

-   **Construção de agentes** que combinam diferentes ferramentas e
    fontes de dados.\
-   **Cadeias (chains)** personalizadas para processamento de texto e
    consultas complexas.\
-   Integração com **APIs externas** (bancos de dados, serviços web ou
    arquivos locais).\
-   **Memória de conversação**, permitindo que o chatbot mantenha
    contexto entre interações.

## 🔧 Tecnologias

-   Python 3.10+\
-   LangChain\
-   OpenAI (ou outro provedor de LLM, configurável)\
-   FastAPI/Flask (opcional, para disponibilizar uma API ou interface
    web)

## 🚀 Como executar

1.  **Clone o repositório**

    ``` bash
    git clone https://github.com/JorgeFCRodrigues/langchain-pytest
    cd nome-do-repo
    ```

2.  **Instale as dependências**

    ``` bash
    pip install -r requirements.txt
    ```

3.  **Configure as variáveis de ambiente** Crie um arquivo `.env` com
    sua chave de API:

        OPENAI_API_KEY=suachave

4.  **Execute o exemplo**

    ``` bash
    python main.py
    ```

## 🗂 Estrutura do Projeto

    ├── main.py          # Script principal de execução
    ├── chains/          # Cadeias personalizadas
    ├── agents/          # Definição de agentes
    ├── requirements.txt # Dependências
    └── README.md

## 📚 Próximos Passos

-   Adicionar interface web com Streamlit ou FastAPI.\
-   Conectar a bancos de dados vetoriais (ex.: Pinecone, FAISS).\
-   Implementar testes automatizados.
