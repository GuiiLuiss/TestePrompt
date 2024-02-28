# Importa os módulos necessários
import os
import sys

# Define uma função para verificar o comprimento do arquivo
def check_file_length(file_path, max_length=20000):
    # Abre o arquivo no caminho especificado com codificação UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # Lê o conteúdo do arquivo
        if len(content) > max_length:  # Verifica se o comprimento excede o máximo permitido
            return False, len(content)  # Retorna False e o comprimento se exceder
    return True, len(content)  # Retorna True e o comprimento se estiver dentro do limite

# Função principal que executa o script
def main():
    # Lê os nomes dos arquivos da variável de ambiente
    files_to_check = os.getenv('MY_VARIABLE')

    # Checa se a variável de ambiente contém nomes de arquivos
    if files_to_check:
        files_to_check = files_to_check.split()  # Converte a string para uma lista de nomes de arquivos
    else:
        # Imprime uma mensagem se não houver arquivos para verificar
        print("Nenhum arquivo modificado ou adicionado para verificar.")
        sys.exit(0)  # Termina o script com sucesso se não houver arquivos para verificar

    all_clear = True  # Inicializa a flag de verificação como True

    # Itera sobre cada caminho de arquivo na lista
    for file_path in files_to_check:
        is_valid, length = check_file_length(file_path)  # Verifica o comprimento do arquivo
        if not is_valid:
            # Imprime uma mensagem se o arquivo exceder o limite de comprimento
            print(f"Arquivo {file_path} excede o limite de 20.000 caracteres com {length} caracteres.")
            all_clear = False  # Atualiza a flag para False se algum arquivo exceder o limite
        else:
            # Imprime uma mensagem se o arquivo estiver dentro do limite
            print(f"Arquivo {file_path} está dentro do limite com {length} caracteres.")

    # Verifica o estado da flag após verificar todos os arquivos
    if not all_clear:
        sys.exit(1)  # Termina com erro se algum arquivo exceder o limite
    else:
        # Imprime uma mensagem se todos os arquivos estiverem dentro do limite
        print("Todos os arquivos modificados/adicionados estão dentro do limite de caracteres.")
        sys.exit(0)  # Termina com sucesso se todos os arquivos estiverem dentro do limite

# Verifica se este script é o principal executado
if __name__ == "__main__":
    main()  # Chama a função principal