# Importa os módulos necessários
import textstat
import os
import sys

# Define uma função para verificar a clareza do arquivo
def check_readability(file_path):
    """Calcula o índice de legibilidade Flesch para o arquivo especificado."""
    # Abre o arquivo no caminho especificado com codificação UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # Lê o conteúdo do arquivo
        readability_score = textstat.flesch_reading_ease(content)  # Calcula o índice de facilidade de leitura Flesch
        return readability_score  # Retorna o valor de clareza do arquivo

# Função principal que executa o script
def main():
    # Lê os nomes dos arquivos da variável de ambiente
    files_to_check = os.getenv('MY_VARIABLE')

    # Checa se a variável de ambiente contém nomes de arquivos
    if files_to_check:
        files_to_check = files_to_check.split()  # Converte a string para uma lista de nomes de arquivos
    else:
        # Imprime uma mensagem se não houver arquivos para verificar
        print("Nenhum arquivo para verificar.")
        sys.exit(0)  # Termina o script com sucesso se não houver arquivos para verificar

    # Itera sobre cada caminho de arquivo na lista
    for file_path in files_to_check:
        readability_score = check_readability(file_path)  # Verifica a clareza do arquivo
        print(f"Índice de Facilidade de Leitura Flesch para {file_path}: {readability_score}")

        # Aplica a lógica de aprovação baseada no índice de legibilidade
        if readability_score >= 46:  # 52 o máximo
            print(f"Texto em {file_path} classificado como FÁCIL de ler. Aprovado.")
        elif readability_score >= 30:
            print(f"Texto em {file_path} classificado como MÉDIO de ler. Aprovado.")
        else:
            print(f"Texto em {file_path} classificado como DIFÍCIL de ler. Reprovado.")
            sys.exit(1)  # Sai com erro imediatamente se algum texto é difícil de ler

if __name__ == "__main__":
    main()
