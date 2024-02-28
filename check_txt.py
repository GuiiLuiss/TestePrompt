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
        return False
    else:
        print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
        return True

def main():
    txt_files = list(glob.glob('./**/*.txt', recursive=True))
    total_files = len(txt_files)
    errors_found = False

    for file_path in txt_files:
        if not check_sections(file_path):
            errors_found = True
            if total_files == 1:  # Se só tem um arquivo, falha imediatamente
                sys.exit(1)

    if errors_found:
        sys.exit(1)  # Falha após verificar todos os arquivos, se algum erro foi encontrado
    else:
        sys.exit(0)  # Sucesso, se nenhum erro foi encontrado

if __name__ == "__main__":
    main()
