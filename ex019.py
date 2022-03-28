from random import choice
msg = ('Exercícios 019')
print(msg)
nome = str(input('Primeiro nome: '))
nome1 = str(input('Segundo nome: '))
nome2 = str(input('terceiro nome: '))
nome3 = str(input('Quarto nome: '))
lista = [nome, nome1, nome2, nome3]
escolhido = choice(lista)
print('O nome escolhido foi? {}!'.format(escolhido))
