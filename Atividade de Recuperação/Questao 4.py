#Um programador está criando um jogo de adivinhação, onde o jogador precisa adivinhar um número secreto entre 1 e 50.
#O programa solicita ao jogador que insira um palpite e informa se o palpite é muito alto ou muito baixo.
#O jogo continua até que o jogador adivinhe o número correto. Escreva um programa em Python que implemente esse jogo.


numeroSecreto = 4
tentativas = 0

print('Adivinhe um numero entre 1 e 50')

while True:
    palpite = int(input('Digite seu palpite: '))
    tentativas += 1

    if palpite > numeroSecreto:
        print('Palpite muito baixo!!!')

    elif palpite < numeroSecreto:
        print('Palpite muito alto!!!')

    else:
        print('Você acertou!! :D')
        break



