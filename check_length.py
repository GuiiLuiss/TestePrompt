import glob
import sys

def check_file_length(file_path, max_length=20000):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if len(content) > max_length:
            print(f"Seu prompt passou o limite {file_path}: {', '.join(content)}")
            sys.exit(1)
        else:
            print(f"O prompt {file_path}. está dentro do padrão de limite de caracteres") 
            sys.exit(0)


def main():
    # Substitua './' pelo diretório específico se necessário, '**/*.txt' busca recursivamente
    for file_path in glob.glob('./**/*.txt', recursive=True):
        check_file_length(file_path)

if __name__ == "__main__":
    main()
