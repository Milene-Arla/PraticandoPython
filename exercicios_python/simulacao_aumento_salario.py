
'''
Precisamos determinar o aumento de salário de funcionário de uma empresa para 10%
'''


cargo = input('Qual seu cargo?').lower()
anosDeEmpresa = int(input('Quantos anos você tem na empresa?'))
salario = int(input('Qual seu salário?'))
if cargo == 'gerente' and anosDeEmpresa >= 1:
    print('parabéns, você recebeu um aumento de 10%. Agora o seu salário é: ', salario + 0.1 * salario)
else:
    print('infelizmente não foi possivel ter aumento esse ano')


