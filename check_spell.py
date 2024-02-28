from spellchecker import SpellChecker
import glob
import sys

def check_spelling(file_path):
    spell = SpellChecker(language='pt')  # Ajuste o idioma conforme necessário
    misspelled_words = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        misspelled = spell.unknown(words)
        for word in misspelled:
            misspelled_words.append(word)
    
    if misspelled_words:
        print(f"Palavras incorretas em {file_path}: {', '.join(misspelled_words)}")
        return False
    return True

def main():
    files_to_check = sys.argv[1:]  # Captura os arquivos passados como argumentos da linha de comando

    # Se nenhum arquivo específico for fornecido, procura por todos os arquivos .txt
    if not files_to_check:
        files_to_check = glob.glob('./**/*.txt', recursive=True)

    all_clear = True  # Flag para acompanhar se todos os arquivos estão livres de erros

    for file_path in files_to_check:
        if not check_spelling(file_path):
            all_clear = False

    if not all_clear:
        sys.exit(1)  # Sair com erro se alguma palavra incorreta for encontrada em qualquer arquivo
    else:
        print("Nenhuma palavra incorreta encontrada em nenhum arquivo.")
        sys.exit(0)  # Sair com sucesso se todas as palavras estiverem corretas

if __name__ == "__main__":
    main()
