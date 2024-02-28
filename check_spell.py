from spellchecker import SpellChecker
import glob
import re
import sys

def preprocess_markdown(content):
    # Remove formatações de negrito e itálico
    content = re.sub(r'\*\*|\*', '', content)
    
    # Mantém apenas o texto de links markdown
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove cabeçalhos Markdown, capturando múltiplos níveis
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
    
    # Remove citações Markdown
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    
    # Remove pontos e vírgulas
    content = re.sub(r'[.,:;]', '', content)
    
    # Adicione mais regras conforme necessário
    return content


def check_spelling(file_path):
    spell = SpellChecker(language='pt')  # Define o idioma para Português
    misspelled_words = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Pré-processa o conteúdo para remover ou ajustar a sintaxe do Markdown
        content = preprocess_markdown(content)
        words = content.split()
        misspelled = spell.unknown(words)
        for word in misspelled:
            misspelled_words.append(word)
    
    if misspelled_words:
        print(f"Palavras incorretas em {file_path}: {', '.join(misspelled_words)}")
        return False
    return True

def main():
    all_clear = True

    for file_path in  glob.glob('./**/*.txt', recursive=True):
        if not check_spelling(file_path):
            all_clear = False

    if not all_clear:
        sys.exit(1)  # Sair com erro se palavras incorretas forem encontradas
    else:
        print("Nenhuma palavra incorreta encontrada em nenhum arquivo.")
        sys.exit(0)  # Sair com sucesso se estiver tudo correto

if __name__ == "__main__":
    main()
