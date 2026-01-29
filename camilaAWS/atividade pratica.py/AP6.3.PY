import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Endereço encontrado:")
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except requests.exceptions.RequestException:
    print("Falha na requisição. Verifique sua conexão.")
