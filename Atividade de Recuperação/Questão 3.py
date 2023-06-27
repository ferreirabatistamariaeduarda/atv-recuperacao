#Uma loja deseja calcular o desconto a ser aplicado em um produto segundo
#a idade do cliente. Se o cliente tiver menos de 21 anos, o desconto será de
#15%. Caso contrário, o desconto será de 10%. Escreva uma função em Python chamada
#"calcular_desconto" que recebe a idade do cliente como parâmetro e retorna o valor
#do desconto a ser aplicado.

produto = float(input('Digite o valor do produto: '))
idade = int(input('Digite sua idade: '))

if idade < 21:
    desconto = produto * (15/100)
    valorFinal = produto - desconto
    print('Parabens, vc ganhou 15% de desconto!!!')
    print('valor com desconto: R$', valorFinal)
else:
    desconto2 = produto * (10 / 100)
    valorFinal2 = produto - desconto2
    print('Parabens, vc ganhou 10% de desconto!!!')
    print('valor com desconto: R$', valorFinal2)

