# Criar uma função que vai receber 2 idades de pessoas diferentes para saber a diferença entre elas. Essa função deve RETORNAR a diferença entre as idades
# Criar outra função que vai exibir na tela (printar) a diferença de idade calculada da função anterior

def calcular_idade(idade1,idade2):
    return idade1 - idade2 # Usei return para retornar o resultado da função calcular_idade

print(calcular_idade(26,25))

def mostrar_diferenca(idade1,idade2):
    print('A diferença de idade é ', calcular_idade(idade1, idade2))

mostrar_diferenca(100,35)

