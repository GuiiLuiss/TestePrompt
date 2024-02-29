import textstat
import os
import sys

def check_readability(file_path):
    """
    Calcula o índice de legibilidade Flesch para o arquivo especificado.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Calcula o índice de facilidade de leitura Flesch
        readability_score = textstat.flesch_reading_ease(content)
        return readability_score

def main():
    files_to_check = os.getenv('MY_VARIABLE')

    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        print("Nenhum arquivo para verificar.")
        sys.exit(0)

    for file_path in files_to_check:
        readability_score = check_readability(file_path)
        print(f"Índice de Facilidade de Leitura Flesch para {file_path}: {readability_score}")

        # Aplica a lógica de aprovação baseada no índice de legibilidade
        if readability_score >= 46: # 52 o máximo
            print(f"Texto em {file_path} classificado como FÁCIL de ler. Aprovado.")
        elif readability_score >= 30:
            print(f"Texto em {file_path} classificado como MÉDIO de ler. Aprovado.")
        else:
            print(f"Texto em {file_path} classificado como DIFÍCIL de ler. Reprovado.")
            sys.exit(1)  # Sai com erro imediatamente se algum texto é difícil de ler

if __name__ == "__main__":
    main()
