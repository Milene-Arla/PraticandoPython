# Função que recebe nome, idade e printa uma apresentação

def apresentar(nome, idade): # A função vai apresentar baseada nos parâmetros (nome, idade)
    print('Oi meu nome é', nome,'e eu tenho', idade,'anos') # Utilizei 'print'para exibir na tela a apresentação
    print('Prazer em te conhecer')


nome = 'Arla' # Criei a variável nome e atribui 'Arla' que é uma string
idade = 25 # criei a variável idade e atribui a ela o número '25' que é um int


apresentar(nome,idade) # Essa é a chamada da função com variáveis
apresentar('Arla', 25) # Essa é a chamda da função com os valores direto
