#Um professor deseja calcular a média de notas de uma turma de 10 alunos. Escreva um programa em Python que solicite ao
#professor as notas dos alunos e, em seguida, calcule e exiba a média das notas. Utilize um laço de repetição (FOR) para
#solicitar as notas dos alunos e uma variável para armazenar a soma das notas.

notas = []
print('MEDIA DE NOTAS')

for i in range(10):
    nota = float(input(f'Digite a nota do {i+1} aluno: '))
    notas.append(nota)

media = sum(notas)/10

print('A media dos alunos eh: ',media)

