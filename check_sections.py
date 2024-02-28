import os
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
        return False  # Retorna False se faltarem seções
    else:
        print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
        return True  # Retorna True se todas as seções estiverem presentes

def main():
    files_to_check = os.getenv('MY_VARIABLE')  # Lê os nomes dos arquivos da variável de ambiente

    if files_to_check:
        files_to_check = files_to_check.split()  # Converte a string em uma lista de nomes de arquivos
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)  # Termina com sucesso se não houver arquivos para verificar

    all_clear = True

    for file_path in files_to_check:
        if not check_sections(file_path):
            all_clear = False

    if not all_clear:
        sys.exit(1)  # Termina com erro se algum arquivo não tiver todas as seções obrigatórias
    else:
        print("Todos os arquivos modificados/adicionados contêm todas as seções obrigatórias.")
        sys.exit(0)  # Termina com sucesso se todos os arquivos estiverem completos

if __name__ == "__main__":
    main()
