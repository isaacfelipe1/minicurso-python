# Define uma função recursiva para calcular o fatorial
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicita a entrada de um número do usuário
num = int(input("Digite um número: "))

# Calcula o fatorial do número
resultado = fatorial(num)

# Exibe o resultado
print("O fatorial de", num, "é", resultado)
