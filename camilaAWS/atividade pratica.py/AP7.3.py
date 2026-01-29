import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    print("Conteúdo do arquivo:\n")
    for index, linha in df.iterrows():
        print(linha.to_string())

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except Exception as erro:
    print("Erro ao ler o arquivo:", erro)

