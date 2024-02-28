# Importa os módulos necessários
import os
import sys

# Define uma função para verificar se as seções obrigatórias estão presentes em um arquivo
def check_sections(file_path):
    # Lista de seções obrigatórias para verificar no arquivo
    required_sections = ["## **Identificação", "## **Personalidade", "## **Contexto"]
    missing_sections = []  # Lista para armazenar seções que estão faltando no arquivo
    
    # Abre o arquivo para leitura com codificação UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # Lê o conteúdo do arquivo
        # Itera sobre cada seção obrigatória para verificar se está presente no conteúdo do arquivo
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)  # Adiciona à lista se a seção estiver faltando
    
    # Verifica se alguma seção obrigatória está faltando
    if missing_sections:
        # Imprime as seções que estão faltando no arquivo
        print(f"Seções faltando em {file_path}: {', '.join(missing_sections)}")
        return False  # Retorna False se faltarem seções
    else:
        # Imprime uma mensagem indicando que todas as seções obrigatórias estão presentes
        print(f"Todas as seções obrigatórias estão presentes em {file_path}.")
        return True  # Retorna True se todas as seções estiverem presentes

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

    # Itera sobre cada caminho de arquivo para verificar as seções obrigatórias
    for file_path in files_to_check:
        if not check_sections(file_path):  # Chama a função de verificação de seções
            all_clear = False  # Atualiza a flag para False se faltarem seções

    # Verifica o estado da flag após verificar todos os arquivos
    if not all_clear:
        sys.exit(1)  # Termina com erro se algum arquivo não tiver todas as seções obrigatórias
    else:
        # Imprime uma mensagem se todos os arquivos contêm todas as seções obrigatórias
        print("Todos os arquivos modificados/adicionados contêm todas as seções obrigatórias.")
        sys.exit(0)  # Termina com sucesso se todos os arquivos estiverem completos

# Verifica se este script é o principal executado
if __name__ == "__main__":
    main()  # Chama a função principal