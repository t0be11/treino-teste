# consome_api_primeiro_ultimo.py
# Substitua 'primeiro_ultimo' pelo seu primeiro e último nome, ex: consome_api_jose_moreira.py

import requests

# Função para consumir a API
def consumir_api(url):
    try:
        print("A invocar a API...")
        resposta = requests.get(url)  # Faz uma requisição GET para a API
        
        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            print("Resposta da API:")
            print(resposta.text)  # Exibe o conteúdo da resposta (como texto)
        else:
            print(f"Erro: A API retornou o código {resposta.status_code}")
    
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao conectar à API: {erro}")

# Programa principal
def main():
    # URL da API
    url_api = "http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa"
    
    # Chamar a função para consumir a API
    consumir_api(url_api)

# Verificar se o ficheiro está a ser executado diretamente
if __name__ == "__main__":
    main()
