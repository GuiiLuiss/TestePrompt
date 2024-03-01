import os
import sys
import re

# Função para verificar a presença de frases longas no texto
def check_long_sentences(file_path, max_words=25):
    """
    Verifica se o arquivo contém frases com mais de 'max_words' palavras.
    Retorna True se todas as frases estiverem dentro do limite, False caso contrário.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Separa o texto em frases usando pontos, exclamações, interrogações e reticências como delimitadores
        sentences = re.split(r'[.!?]+|(?<!\.)\.{3}(?!\.)', content)
        long_sentences = [sentence for sentence in sentences if len(sentence.split()) > max_words]

        if long_sentences:
            return False, len(long_sentences)  # Retorna False e a quantidade de frases longas
    return True, 0  # Retorna True se não houver frases longas

def main():
    files_to_check = os.getenv('MY_VARIABLE')

    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    all_clear = True

    for file_path in files_to_check:
        # Verifica a presença de frases longas
        sentences_ok, long_count = check_long_sentences(file_path)
        if not sentences_ok:
            print(f"Arquivo {file_path} contém {long_count} frases com mais de 25 palavras, o que pode afetar a concisão.")
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
