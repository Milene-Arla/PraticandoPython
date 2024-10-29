# Considerando que existe uma lista de preços de produtos. Para cada produto, caso o valor seja maior que 100 reais, exiba "Produto caro", se não, exiba "Produto barato"

precos = [100,200,50,500,10,5,85,60,90]

def categorizar_produto(x):
      if x > 100:
       print('Produto caro')
      else:
       print('Produto barato')

for preco in precos: 
   categorizar_produto(preco)