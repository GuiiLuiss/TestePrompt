import glob
import sys

def check_sections(file_path):
    required_sections = ["## **Identificação", "## **Personalidade", "## **Contexto"]  # Exemplo de seções obrigatórias
    missing_sections = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)

    if missing_sections:
        print(f"Seções faltando em {file_path}: {', '.join(missing_sections)}")
        sys.exit(1)
    else:
        print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
        sys.exit(0)

def main():
    # Substitua './' pelo diretório específico se necessário, '**/*.txt' busca recursivamente
    for file_path in glob.glob('./**/*.txt', recursive=True):
        check_sections(file_path)

if __name__ == "__main__":
    main()