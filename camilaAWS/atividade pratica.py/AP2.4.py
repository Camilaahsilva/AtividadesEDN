distancia = float(input("Digite a distância percorrida (km): "))
combustivel = float(input("Digite o combustível gasto (litros): "))

consumo_medio = distancia / combustivel

print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", round(consumo_medio, 2), "km/l")