numeros_favoritos = {}

colegas = ['Joao', 'Caio', 'Bruno', 'Roberto', 'Felipe']

for colega in colegas:
    numero_favorito = input(f'Qual é o numéro favorito de {colega}?')
    numeros_favoritos[colega] = numero_favorito

print("Números favoritos dos colegas:")
for nome, numero in numeros_favoritos.items():
    print(f"{nome}: {numero}")
