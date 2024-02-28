import glob
import sys

def check_sections(file_path):
    required_sections = ["## **Identificação**", "## **Personalidade**", "## **Contexto**"]
    missing_sections = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)

    if missing_sections:
        print(f"Seções faltando em {file_path}: {', '.join(missing_sections)}")
        return False  # Retornar False em vez de chamar sys.exit(1)
    else:
        print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
        return True

def main():
    errors = False
    for file_path in glob.glob('./**/*.txt', recursive=True):
        if not check_sections(file_path):
            errors = True  # Marcar que encontramos erros

    if errors:
        sys.exit(1)  # Terminar com código de saída de falha se algum erro foi encontrado
    else:
        sys.exit(0)  # Terminar com sucesso se nenhum erro foi encontrado

if __name__ == "__main__":
    main()
