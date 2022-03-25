from sys import flags


msg = ('exercício 014')
print(msg)
c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5)+32
print('A temperatura de {} ºC corresponde a {} ºF!'.format(c, f))
