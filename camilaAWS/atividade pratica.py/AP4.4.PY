# Atividade Prática 04
# AP4.4 - Analisador de números pares e ímpares

quantidade = int(input("Quantos números deseja digitar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

