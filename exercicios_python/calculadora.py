'''
Criar uma calculadora. Nesse exercício receberemos como entrada o tipo de operação que o cliente quer fazer,
os 2 números que ele escolher, e iremos retornar o resultado da operação.
    Operações aceitas: Adição, Multiplicação, Divisão e Subtração
'''

'''
OBSERVAÇÃO:
    if (condição):
       blablabla
    if(condicao):
        blablabla
    if(condicao):
        blablabla
'''
primeiroNumero = int(input('qual seu primeiro número? '))
segundoNumero = int(input('qual seu segundo número? '))
operacao = input('Qual operação você quer? Você tem as opções de: adição, multiplicação, divisão e subtração ').lower()
if operacao == 'adição':
    print('O seu resultado é', primeiroNumero+segundoNumero)
elif operacao == 'multiplicação':
    print('o seu resultado é', primeiroNumero*segundoNumero)
elif operacao == 'divisão':
    print('o seu resultado é', primeiroNumero/segundoNumero)
elif operacao == 'subtração':
    print('o seu resultado é', primeiroNumero-segundoNumero)
else:
    print('essa calculadora não faz esse tipo de operação')




