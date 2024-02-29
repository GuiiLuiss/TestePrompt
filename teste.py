import textstat
import os
import sys

textstat.set_lang("pt")

def check_readability(file_path):
    """
    Calcula o índice de legibilidade Flesch-Kincaid para o arquivo especificado.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
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
        print(f"Índice de Legibilidade Flesch-Kincaid para {file_path}: {readability_score}")

if __name__ == "__main__":
    main()
