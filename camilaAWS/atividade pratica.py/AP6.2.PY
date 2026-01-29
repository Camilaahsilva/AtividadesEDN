import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # verifica erro de conexão

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Usuário gerado com sucesso!")
    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("Falha ao conectar à API. Tente novamente mais tarde.")
