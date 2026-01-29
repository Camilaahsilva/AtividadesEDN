import pandas as pd

# Dados das pessoas
dados = {
    "Nome": ["Ana", "Bruno", "Carla", "Daniel"],
    "Idade": [25, 30, 22, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

df = pd.DataFrame(dados)

arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

try:
    df.to_csv(arquivo, index=False)
    print("Arquivo salvo com sucesso!")

except Exception as erro:
    print("Erro ao salvar o arquivo:", erro)
