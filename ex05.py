numeros = []

for i in range(5):
    numero = int(input(f"Informe o {i+1}º número inteiro: "))
    numeros.append(numero)

print("Os números informados são:")
for numero in numeros:
    print(numero)
