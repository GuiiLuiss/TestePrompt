import os
import sys
import re

def check_long_sentences(file_path, max_words=25):
    """
    Verifica se o arquivo contém frases com mais de 'max_words' palavras.
    Retorna False e detalhes das frases longas se encontradas, True e vazio caso contrário.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        sentences = re.split(r'[.!?]+|(?<!\.)\.{3}(?!\.)', content)
        
        # Inicializa uma lista para armazenar detalhes das frases longas
        long_sentences_details = []
        
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            if len(words) > max_words:
                # Armazena a frase e sua contagem aproximada de linha baseada em quebras de linha anteriores
                line_count = content[:content.find(sentence)].count('\n') + 1
                long_sentences_details.append((i+1, line_count, ' '.join(words)))

        if long_sentences_details:
            return False, long_sentences_details
    return True, []

def main():
    files_to_check = os.getenv('MY_VARIABLE')

    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    all_clear = True

    for file_path in files_to_check:
        sentences_ok, long_sentences_details = check_long_sentences(file_path)
        if not sentences_ok:
            print(f"Arquivo {file_path} contém frases longas:")
            for detail in long_sentences_details:
                sentence_number, line_count, sentence = detail
                print(f"  Frase {sentence_number} (aprox. linha {line_count}): {sentence[:50]}...")
            all_clear = False
        else:
            print(f"Arquivo {file_path} está dentro dos limites de comprimento de frase.")

    if not all_clear:
        sys.exit(1)
    else:
        print("Todos os arquivos verificados estão dentro dos limites de comprimento de frase.")
        sys.exit(0)

if __name__ == "__main__":
    main()
