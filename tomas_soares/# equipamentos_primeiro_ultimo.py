# equipamentos_primeiro_ultimo.py
# Substitua 'primeiro_ultimo' pelo seu primeiro e último nome, ex: jose_moreira

# a) Abrir o ficheiro devices.txt e guardar os equipamentos numa lista
def carregar_equipamentos(nome_ficheiro):
    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            equipamentos = [linha.strip() for linha in ficheiro if linha.strip()]
        return equipamentos
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado!")
        return []

# c) Procurar o equipamento na lista
def procurar_equipamento(lista_equipamentos):
    while True:
        resposta = input("Equipamento a procurar (sair p/terminar): ").strip()
        
        if resposta.lower() == "sair":
            print("Programa terminado.")
            break
        
        # d) Procurar na lista e contar ocorrências
        encontrados = [equipamento for equipamento in lista_equipamentos if resposta.lower() in equipamento.lower()]
        
        if encontrados:
            print(f"Equipamentos encontrados ({len(encontrados)}):")
            for eq in encontrados:
                print(f"- {eq}")
        else:
            print("Equipamento Não existe na Lista!")

# Programa principal
def main():
    # Nome do ficheiro a ser lido
    nome_ficheiro = "devices.txt"
    
    # Carregar os equipamentos
    equipamentos = carregar_equipamentos(nome_ficheiro)
    
    if equipamentos:  # Só continua se a lista não estiver vazia
        print("Equipamentos carregados com sucesso!")
        procurar_equipamento(equipamentos)
    else:
        print("Não foi possível carregar os equipamentos. O programa será encerrado.")

# Chamar a função principal
if __name__ == "__main__":
    main()
