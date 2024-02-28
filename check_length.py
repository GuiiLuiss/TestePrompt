import os
import glob
import sys

def check_file_length(file_path, max_length=20000):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if len(content) > max_length:
            return False, len(content)
    return True, len(content)

def main():
    files_to_check = os.getenv('MY_VARIABLE')  # Lê os nomes dos arquivos da variável de ambiente

    if files_to_check:
        files_to_check = files_to_check.split()  # Converte a string para uma lista de nomes de arquivos
    else:
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)  # Termina com sucesso se não houver arquivos para verificar

    all_clear = True

    for file_path in files_to_check:
        is_valid, length = check_file_length(file_path)
        if not is_valid:
            print(f"Arquivo {file_path} excede o limite de 20.000 caracteres com {length} caracteres.")
            all_clear = False
        else:
            print(f"Arquivo {file_path} está dentro do limite com {length} caracteres.")

    if not all_clear:
        sys.exit(1)  # Termina com erro se algum arquivo exceder o limite
    else:
        print("Todos os arquivos modificados/adicionados estão dentro do limite de caracteres.")
        sys.exit(0)  # Termina com sucesso

if __name__ == "__main__":
    main()
