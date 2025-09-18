# agent.py
import os
import sys
from generator import TestGenerator

def main():
    if len(sys.argv) < 2:
        print("Uso: python agent.py <caminho_para_arquivo_python>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"Arquivo não encontrado: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()

    output_dir = os.environ.get("OUTPUT_DIR", "outputs")
    os.makedirs(output_dir, exist_ok=True)

    gen = TestGenerator()
    test_filename, test_content = gen.generate_tests_from_code(code, source_path=input_path)

    output_path = os.path.join(output_dir, test_filename)
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(test_content)

    print(f"Arquivo de testes gerado: {output_path}")

if __name__ == "__main__":
    main()
