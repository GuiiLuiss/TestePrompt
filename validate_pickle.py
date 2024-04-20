import pickle
import sys

def load_data_pickle(file_path):
    """Carrega dados de um arquivo pickle."""
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Erro ao carregar o arquivo pickle: {e}", file=sys.stderr)
        sys.exit(1)  # Sair com status de erro para garantir que o GitHub Actions capture o falha

def validate_data(data):
    """Valida o conteúdo do dicionário de dados extraído do arquivo pickle."""
    expected_keys = ['params', 'metrics', 'artifacts', 'tags']
    for key in expected_keys:
        if key not in data:
            print(f"Chave obrigatória '{key}' ausente no arquivo pickle.", file=sys.stderr)
            sys.exit(1)  # Sair com status de erro
    
    # Validações adicionais para cada seção
    if not isinstance(data['params'], dict):
        print("A seção 'params' deve ser um dicionário.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data['metrics'], dict):
        print("A seção 'metrics' deve ser um dicionário.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data['artifacts'], dict):
        print("A seção 'artifacts' deve ser um dicionário.", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data['tags'], dict):
        print("A seção 'tags' deve ser um dicionário.", file=sys.stderr)
        sys.exit(1)

    print("Validação concluída com sucesso para o arquivo pickle.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_pickle.py <caminho_para_o_arquivo_pickle>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    data = load_data_pickle(file_path)
    validate_data(data)
