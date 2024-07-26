# Define uma função para calcular a média
def calcular_media(numeros):
    total = sum(numeros)
    media = total / len(numeros)
    return media

# Solicita a entrada de uma lista de números do usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]

# Calcula a média dos números
media = calcular_media(numeros)

# Exibe o resultado
print("A média dos números é", media)
