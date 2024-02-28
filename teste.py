import subprocess
import os
import sys

# Função para executar comandos PromptFoo via linha de comando
def run_promptfoo_eval(file_path):
    try:
        # Substitua 'promptfooconfig.yaml' pelo caminho do seu arquivo de configuração real, se necessário
        result = subprocess.run(['promptfoo', 'eval', '-p', file_path, '-c', 'promptfooconfig.yaml'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar PromptFoo para o arquivo {file_path}:", e.output)

# Sua função principal modificada
def main():
    files_to_check = os.getenv('MY_VARIABLE')
    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    all_clear = True

    for file_path in files_to_check:
        # Aqui você pode manter a verificação do tamanho do arquivo ou qualquer outra lógica prévia
        # E depois adicionar a chamada para avaliar o prompt com o PromptFoo
        run_promptfoo_eval(file_path)

    if not all_clear:
        sys.exit(1)
    else:
        print("Todos os arquivos modificados/adicionados estão dentro do limite de caracteres.")
        sys.exit(0)

if __name__ == "__main__":
    main()
