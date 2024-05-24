
num_alunos = 10

medias = []


for i in range(num_alunos):
    print(f"Informações do aluno {i+1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias.append(media)

alunos_aprovados = sum(1 for media in medias if media >= 7.0)


print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")
