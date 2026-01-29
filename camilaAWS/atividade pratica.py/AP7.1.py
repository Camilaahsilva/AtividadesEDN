import pandas as pd

arquivo = "logs_treinamento.csv"

try:
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()

    print("Resultado da análise:")
    print("Média do tempo de execução:", round(media, 2))
    print("Desvio padrão:", round(desvio, 2))

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except Exception as erro:
    print("Erro ao ler o arquivo:", erro)

