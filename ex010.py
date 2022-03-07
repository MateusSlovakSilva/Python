msg = ('Conversor de moeda na data de 25/02/22')
print(msg)

r = float(input('Valor em Real: '))
dolar = r / 5.16
Euro = r / 5.82
Libra = r / 6.93
Iane = r / 0.045
Rublorusso = r / 0.062
print('Valor em Real {} da {:.2f} Dolar.'.format(r,dolar))
print('Valor em Real {} da {:.2f} Euros'.format(r,Euro))
print('Valor em Real {} da {:.2f} Libra'.format(r,Libra))
print('Valor em Real {} da {:.2f} Iane'.format(r,Iane))
print('Valor em Real {} da {:.2f} Rublo Russo'.format(r, Rublorusso))