valor_reais = float(input("Digite o valor em reais: "))

taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em dólares:", round(valor_dolar, 2))
print("Valor em euros:", round(valor_euro, 2))