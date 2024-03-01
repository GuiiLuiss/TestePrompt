# Importa os módulos necessários para o script
import os
import sys
import re

def check_long_sentences(file_path, max_words=75):
    """
    Verifica se o arquivo contém frases com mais de 75 palavras.
    Retorna False e detalhes das frases longas se encontradas, True e vazio caso contrário.
    """
    # Abre o arquivo para leitura e armazena seu conteúdo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Divide o conteúdo do arquivo em frases usando expressões regulares
        sentences = re.split(r'[.!?#]+|(?<!\.)\.{3}(?!\.)', content)
        
        # Inicializa uma lista para armazenar detalhes das frases longas
        long_sentences_details = []
        
        # Itera sobre cada frase para verificar seu comprimento
        for i, sentence in enumerate(sentences):
            words = sentence.split()
            # Verifica se a frase tem mais palavras do que o máximo permitido
            if len(words) > max_words:
                # Calcula a linha aproximada onde a frase longa começa
                line_count = content[:content.find(sentence)].count('\n') + 1
                # Armazena o número da frase, a linha aproximada e a frase em si
                long_sentences_details.append((i+1, line_count, ' '.join(words)))

        # Retorna False e os detalhes se frases longas forem encontradas
        if long_sentences_details:
            return False, long_sentences_details
    # Retorna True e uma lista vazia se todas as frases estiverem dentro do limite
    return True, []

def main():
    # Obtém uma variável de ambiente que contém os arquivos a serem verificados
    files_to_check = os.getenv('MY_VARIABLE')

    # Divide a string de arquivos em uma lista, se existir
    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        # Se não houver arquivos para verificar, termina o script
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    # Flag para acompanhar se todos os arquivos estão dentro dos limites
    all_clear = True

    # Itera sobre cada arquivo para verificar as frases longas
    for file_path in files_to_check:
        sentences_ok, long_sentences_details = check_long_sentences(file_path)
        # Se frases longas forem encontradas, imprime os detalhes
        if not sentences_ok:
            print(f"Arquivo {file_path} contém frases longas:")
            for detail in long_sentences_details:
                sentence_number, line_count, sentence = detail
                # Imprime uma prévia da frase longa com sua localização aproximada
                print(f"  Frase {sentence_number} (aprox. linha {line_count}): {sentence[:50]}...")
            all_clear = False
        else:
            # Se não houver frases longas, informa que o arquivo está ok
            print(f"Arquivo {file_path} está dentro dos limites de comprimento de frase.")

    # Se alguma frase longa foi encontrada, termina o script com erro
    if not all_clear:
        sys.exit(1)
    else:
        # Se todos os arquivos estão dentro dos limites, termina o script com sucesso
        print("Todos os arquivos verificados estão dentro dos limites de comprimento de frase.")
        sys.exit(0)

# Garante que o script só será executado se chamado diretamente
if __name__ == "__main__":
    main()






