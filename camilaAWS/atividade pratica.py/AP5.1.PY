# Atividade Prática 05
# AP5.1 - Cálculo de gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Programa principal
valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)

print("Valor da gorjeta:", valor_gorjeta)
