
rendaMensal = int(input('Qual sua renda mensal?'))
valorInvestido = int(input('Qual seu valor investido?'))
idade = int(input('Qual sua idade?'))
if rendaMensal >= 5000 and valorInvestido > 10000 and idade > 18:
    print('Parabéns! Você se tornou um cliente do Banco')
else:
    print('Infelizmente não poderemos prosseguir com a abertura da s'
          'ua conta. Qualquer dúvida, entre em contato conosco.')