#Uma empresa deseja verificar se um determinado cupom está dentro da faixa de
# cupons gerados para a promoção de São João. Caso o número esteja dentro do intervalo,
# o programa deve exibir a mensagem "Cupom válido". Caso contrário, deve exibir a mensagem "Cupom inválido",
# sabendo que o primeiro cupom tinha o número 75 e o último gerado foi o 208. Escreva um programa em Python
# que recebe o número inteiro do cupom e verifique se o cupom é válido.

print('Verificação de Cupom')

num = int(input('Digite seu cupom: '))
if 75 <= num <= 208:
    print('Cupom Válido!!! ')
else:
    print('Cupom Inválido :(')



