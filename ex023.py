msg = ('Exercícios 023')
print(msg)
numero = int(input('Informe um número: '))
u = numero // 1 % 10
d = numero //10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o número {}.'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
