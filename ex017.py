from math import hypot
msg = ('exercício 017')
print(msg)
'''catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadiacente= float(input('Comprimento do cateto adiacente: '))
hipotenusa = (catetooposto ** 2 + catetoadiacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''
catetooposto = float(input('Comprimento do cateto oposto: '))
catetoadiacente = float(input('Comprimento do cateto adiacente: '))
hipotenusa = hypot(catetooposto, catetoadiacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
