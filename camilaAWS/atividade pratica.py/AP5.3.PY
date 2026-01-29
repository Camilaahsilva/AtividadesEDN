# Atividade Prática 05
# AP5.3 - Cálculo de preço com desconto

def calcular_preco_final(preco_original, desconto_percentual):
    desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - desconto
    return preco_final


# Programa principal
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))

valor_final = calcular_preco_final(preco, desconto)

print("Preço final do produto:", valor_final)
