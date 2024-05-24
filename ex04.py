num_alunos = 30


idades = []
alturas = []

for i in range(num_alunos):
    idade = int(input(f"Informe a idade do aluno {i+1}: "))
    altura = float(input(f"Informe a altura (em metros) do aluno {i+1}: "))
    idades.append(idade)
    alturas.append(altura)


media_altura = sum(alturas) / num_alunos

alunos_contados = sum(1 for i in range(num_alunos) if idades[i] > 13 and alturas[i] < media_altura)

print(f"O número de alunos com mais de 13 anos e altura inferior à média é: {alunos_contados}")
