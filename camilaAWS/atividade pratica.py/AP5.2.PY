# Atividade Prática 05
# AP5.2 - Verificador de Palíndromo

def eh_palindromo(texto):
    texto_limpo = ""

    for caractere in texto:
        if caractere.isalnum():  # ignora espaços e pontuação
            texto_limpo += caractere.lower()

    return texto_limpo == texto_limpo[::-1]


# Programa principal
frase = input("Digite uma palavra ou frase: ")

if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
