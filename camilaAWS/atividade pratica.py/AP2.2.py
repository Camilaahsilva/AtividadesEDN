nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original do produto: "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco_original * desconto_percentual / 100
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))