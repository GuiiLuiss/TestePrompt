# Importa os módulos necessários para o script
import os
import subprocess
import sys

def check_spelling(file_path, lang='pt_BR'):
    """
    Verifica a ortografia do arquivo usando Hunspell.
    """
    # Define o comando para executar o Hunspell com um dicionário personalizado e a língua especificada
    cmd = f"hunspell -d {lang},custom -p ./custom.dic -l"
    
    # Abre o arquivo para leitura e armazena seu conteúdo
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Executa o Hunspell passando o conteúdo do arquivo como entrada
    result = subprocess.run(cmd, input=content, text=True, capture_output=True, shell=True)
    
    # Processa a saída do Hunspell para obter as palavras incorretas, removendo duplicatas
    incorrect_words = set(word.lower() for word in result.stdout.strip().split('\n') if word)
    
    # Se palavras incorretas forem encontradas, imprime-as e retorna False
    if incorrect_words:
        print(f"Arquivo {file_path} contém palavras incorretas:")
        for word in incorrect_words:
            print(f"  {word}")
        return False
    # Se não houver palavras incorretas, retorna True
    return True

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

    # Flag para acompanhar se todos os arquivos estão corretos ortograficamente
    all_clear = True

    # Itera sobre cada arquivo para verificar a ortografia
    for file_path in files_to_check:
        spelling_ok = check_spelling(file_path)
        # Se houver erros de ortografia, atualiza a flag para False
        if not spelling_ok:
            all_clear = False

    # Se algum erro de ortografia foi encontrado, termina o script com erro
    if not all_clear:
        sys.exit(1)
    else:
        # Se todos os arquivos estão corretos ortograficamente, termina o script com sucesso
        print("Todos os arquivos verificados estão corretos ortograficamente.")
        sys.exit(0)

# Garante que o script só será executado se chamado diretamente
if __name__ == "__main__":
    main()
