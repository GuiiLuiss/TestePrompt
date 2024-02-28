import glob

def check_sections(file_path):
    required_sections = ["## **Identificação**", "## **Personalidade", "## **Contexto**"]  # Exemplo de seções obrigatórias
    missing_sections = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)

    if missing_sections:
        print(f"Missing sections in {file_path}: {', '.join(missing_sections)}")
        return False
    else:
        print(f"All required sections are present in {file_path}.")
        return True

def main():
    # Substitua './' pelo diretório específico se necessário, '**/*.txt' busca recursivamente
    for file_path in glob.glob('./**/*.txt', recursive=True):
        check_sections(file_path)

if __name__ == "__main__":
    main()