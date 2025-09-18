# generator.py
import os
from typing import Tuple
try:
    from langchain.chat_models import AzureChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage
except Exception as e:
    raise ImportError(
        "langchain não encontrado. Instale com: pip install langchain"
    ) from e

class TestGenerator:
    def __init__(self):
        azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
        azure_base = os.environ.get("AZURE_OPENAI_ENDPOINT")
        deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
        if not all([azure_api_key, azure_base, deployment]):
            raise EnvironmentError(
                "Defina AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_NAME no .env"
            )
        self.client = AzureChatOpenAI(
            deployment_name=deployment,
            temperature=float(os.environ.get("TEMPERATURE", "0.0")),
            max_retries=2,
        )

    def _suggest_test_filename(self, source_path: str) -> str:
        import os
        name = os.path.splitext(os.path.basename(source_path))[0]
        return f"test_{name}.py"

    def _build_prompt(self, code: str, source_path: str) -> str:
        return f"""Você é um gerador de testes pytest.
Retorne apenas o arquivo de teste começando com 'import pytest'.
Crie funções def test_* para sucesso e falha.
Código:
```
{code}
```
"""

    def generate_tests_from_code(self, code: str, source_path: str = "input.py") -> Tuple[str, str]:
        system_msg = SystemMessage(content="Você é um assistente que gera arquivos pytest.")
        human_msg = HumanMessage(content=self._build_prompt(code, source_path))
        response = self.client.predict_messages([system_msg, human_msg])
        content = response.content if hasattr(response, "content") else str(response)
        if not content.lstrip().startswith("import pytest"):
            content = "import pytest\n\n" + content
        return self._suggest_test_filename(source_path), content
