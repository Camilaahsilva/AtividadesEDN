tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
        break

    except ValueError:
        tentativas += 1
        print(f"Erro: digite apenas números. Tentativas {tentativas}/3\n")

    except ZeroDivisionError:
        tentativas += 1
        print(f"Erro: não é possível dividir por zero. Tentativas {tentativas}/3\n")

if tentativas == max_tentativas:
    print("Número máximo de tentativas atingido. Encerrando o programa")