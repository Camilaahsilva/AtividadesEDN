import requests
from datetime import datetime

moeda = input("Digite a moeda (ex: USD, EUR, BTC): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        cotacao = dados[chave]

        valor_atual = cotacao["bid"]
        maxima = cotacao["high"]
        minima = cotacao["low"]
        data_hora = datetime.fromtimestamp(int(cotacao["timestamp"]))

        print("Cotação da moeda:", moeda)
        print("Valor atual (BRL):", valor_atual)
        print("Máxima:", maxima)
        print("Mínima:", minima)
        print("Última atualização:", data_hora)

except requests.exceptions.RequestException:
    print("Erro ao consultar a cotação. Verifique sua conexão.")
