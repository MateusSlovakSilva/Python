from random import randint
from time import sleep #demora um pouco para responder
msg = ('Exercícios 028')
print(msg)
computador = randint(0,5)
print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você consegui me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
