# Considerando o gasto do cartão e a renda do cliente, avaliar se ele pode financiar uma casa ou não.
# Você vai receber do cliente o valor do gasto do cartão e o valor da renda dele. O gasto do cartão tem que ser menor que 5000 e a renda tem que ser maior que 10000

def validar_financiamento(g, r):
   if g <= 5000 and r >= 10000:
      print('Parabêns, você pode financiar uma casa')
   else:
      print('infelizmente o seu financiamenento foi negado')

  
valor1 = int(input('Qual valor do gasto do seu cartão? '))
valor2 = int(input('Qual valor da sua renda?  '))

validar_financiamento(valor1, valor2)

  