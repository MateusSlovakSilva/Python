from datetime import date # pega o ano atual do computador
msg = ('\033[1;4;35mExercícios 032\033[m')
print(msg)
ano = int(input('Que ano quer analisar? '))
if ano  == 0:
    ano = date.today().year # esse comando vai pegar o ano atual do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[1;32mBISSEXTO\033[m'.format(ano))
else:
    print('O ano {} \033[1;31mNÃO é BISSEXTO\033[m'.format(ano))
