#Uma livraria deseja listar os livros mais vendidos do mês no
#padrão POSIÇÃO - TÍTULO DO LIVRO. Escreva um programa em Python que
#receba uma lista de livros com sua respectiva posição no ranking dos
#mais vendidos e exiba essa lista em tela, conforme o exemplo a seguir.
#Ranking de Mais Vendidos
#1 - Senhor dos Anéis
#2 - O apanhador no campo de centeio

rank = {}

print('RANKING DE LIVROS')

qnt = int(input('quantidade de livros: '))

for i in range(qnt):
    posicao = input('Digite a posicao do livro: ')
    livro = input('Digite o nome do livro: ')
    rank[int(posicao)] = livro

print('Ranking')
for posicao in sorted(rank):
    livro = rank[posicao]
    print(f'{posicao}-{livro}')







