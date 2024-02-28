import subprocess
import os
import json
import sys

def run_promptfoo_eval(file_path):
    try:
        # Adapte os argumentos conforme necessário para sua configuração
        result = subprocess.run(['promptfoo', 'eval', '-p', file_path, '--no-cache'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar PromptFoo para o arquivo {file_path}:", e.stderr)
        sys.exit(1)

def main():
    files_to_check = json.loads(os.getenv('MY_VARIABLE', '[]'))

    if not files_to_check:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    for file_path in files_to_check:
        run_promptfoo_eval(file_path)

    print("Avaliação de prompts concluída com sucesso.")

if __name__ == "__main__":
    main()
