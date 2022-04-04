msg = ('\033[1;4;35mExercícios 034\033[m')
print(msg)
salario = float(input('Digite seu salario: '))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$\033[31m{:.2f}\033[m passa a ganhar R$\033[32m{:.2f}\033[m agora'.format(salario, novo))
