# Criar uma função que vai retornar a soma do número de balas que 2 pessoas tem
# Criar outra função que vai exibir na tela (printar) quantas balas as 2 pessoas tem juntas

def calcular_total_balas(numero1, numero2):
    return numero1 + numero2

#print(calcular_total_balas(10,30))

def exibir_resultado(numero1,numero2):
    print('Juntas temos', calcular_total_balas(numero1,numero2), 'balas')

numero1 = int(input('Qual é o primeiro número? '))
numero2 = int(input('Qual é o segundo número? '))

exibir_resultado(numero1,numero2)

