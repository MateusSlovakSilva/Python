msg = ('\033[1;4;35mExercícios 035\033[m')
print(msg)
casa = float(input('\033[1;33mValor da casa?\033[m '))
salario = float(input('\033[1;33mSálario do Comprador?\033[m '))
anos = int(input('\033[1;33mQuantos anos de financiamento?\033[m '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$\033[32m{:.2f}\033[m em \033[32m{}\033[m anos, a prestação de R$\033[32m{:.2f}\033[m'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Empréstimo pode ser \033[1;4;32mCONCEDIDO\033[m')
else:
    print('Empréstimo \033[1;2;31mNEGADO\033[m')
