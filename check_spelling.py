import os
import subprocess
import sys

def check_spelling(file_path, lang='pt_BR'):
    """
    Verifica a ortografia do arquivo usando Hunspell.
    """
    # Comando para verificar a ortografia com Hunspell
    cmd = f"hunspell -d {lang} -l"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Executa o Hunspell
    result = subprocess.run(cmd, input=content, text=True, capture_output=True, shell=True)
    
    # Captura as palavras incorretas
    incorrect_words = result.stdout.strip().split('\n')
    
    if incorrect_words:
        print(f"Arquivo {file_path} contém palavras incorretas:")
        for word in incorrect_words:
            print(f"  {word}")
        return False
    return True

def main():
    files_to_check = os.getenv('MY_VARIABLE')

    if files_to_check:
        files_to_check = files_to_check.split()
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)

    all_clear = True

    for file_path in files_to_check:
        spelling_ok = check_spelling(file_path)
        if not spelling_ok:
            all_clear = False

    if not all_clear:
        sys.exit(1)
    else:
        print("Todos os arquivos verificados estão corretos ortograficamente.")
        sys.exit(0)

if __name__ == "__main__":
    main()
