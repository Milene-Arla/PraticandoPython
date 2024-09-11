'''
    Simulação de envio de notificação 5x pro cliente
'''
import time

contador = 1
while contador<=5:
    contador = contador + 1
    print(contador)
    time.sleep(1)
    print('Parabéns você se tornou um cliente 5 estrelas')