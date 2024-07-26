# Solicita a entrada de uma lista de números do usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]

# Inicializa a variável maior com o primeiro elemento da lista
maior = numeros[0]

# Percorre a lista para encontrar o maior número
for num in numeros:
    if num > maior:
        maior = num

# Exibe o maior número
print("O maior número na lista é", maior)
