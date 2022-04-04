msg = ('\033[1;4;35mExercícios 033\033[m')
print(msg)
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
#verificando menor
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando maior 
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))

