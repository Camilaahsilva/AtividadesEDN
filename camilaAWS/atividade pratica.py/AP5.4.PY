from datetime import date

# Entrada de dados
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))
ano = int(input("Digite o ano do nascimento: "))

# Data de nascimento
data_nascimento = date(ano, mes, dia)

# Data atual
data_atual = date.today()

# Cálculo da diferença em dias
dias_vivo = (data_atual - data_nascimento).days

# Saída
print(f"Você está vivo(a) há {dias_vivo} dias.")

