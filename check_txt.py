import sys

def check_sections(file_path):
    required_sections = ["## **Identificação", "## **Personalidade", "## **Contexto"]
    missing_sections = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for section in required_sections:
                if section not in content:
                    missing_sections.append(section)

        if missing_sections:
            print(f"Seções faltando em {file_path}: {', '.join(missing_sections)}")
            return False
        else:
            print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
            return True
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return False

def main():
    files_to_check = sys.argv[1:]  # Captura os arquivos passados como argumentos
    errors_found = False

    for file_path in files_to_check:
        if not check_sections(file_path):
            errors_found = True

    if errors_found:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
