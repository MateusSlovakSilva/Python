from random import randint
from time import sleep
msg = ('\033[1;4;35mExercicio 045\033[m')
print(msg)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''\033[1;36mSuas opções:\033[m
\033[1;33m[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('Qual é sua jogada? '))
print('\033[1;36mJO\033[m')
sleep(1)
print('\033[1;36mKEN\033[m')
sleep(1)
print('\033[1;36mPO!!!\033[m')
print('\033[32m-=\033[m'*15)
print('O computador escolheu \033[1;31m{}\033[m'.format(itens[computador]))
print('O jogador jogou \033[1;34m{}\033[m'.format(itens[jogador]))
print('\033[32m-=\033[m'*15)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[1;35mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif jogador == 1:
        print('\033[1;35mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m') 

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[1;32mVOCÊ VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif jogador == 2:
        print('\033[1;35mEMPATE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
