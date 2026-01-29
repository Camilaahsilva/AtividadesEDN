# Atividade Prática 05
# AP5.3 - Cálculo de preço final com desconto percentual

# Entrada de dados
preco_original = float(input("Digite o preço original do produto: R$ "))
desconto_percentual = float(input("Digite o desconto (%): "))

# a - Cálculo do desconto
valor_desconto = preco_original * (desconto_percentual / 100)

# b - Preço final após o desconto
preco_final = preco_original - valor_desconto

# c - Arredondamento para 2 casas decimais
preco_final = round(preco_final, 2)

# d - E
