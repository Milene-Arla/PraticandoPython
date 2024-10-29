# Considerando uma lista de renda, avaliar se o cliente pode ou não ter um cartão de crédito no banco baseado na sua renda
# A renda para ter um cartão de crédito deve ser maior que 5000 reais

rendas_clientes = [1000,6000,8000,10000,800,1500]

def avaliar_credito(x):
    if x > 5000:
         print('Parabéns, você foi aprovado!')
    else:
        print('Você não foi aprovado! tente novamente dentro de 3 meses.')

for renda in rendas_clientes: 
    avaliar_credito(renda)
   