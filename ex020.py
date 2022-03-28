from random import shuffle     #shuffle vai organizar uma ordem aleatoria.
msg = ('Exercícios 020')
print(msg)
nome = str(input('Primeiro nome: '))
nome1 = str(input('Segundo nome: '))
nome2 = str(input('Terseiro nome: '))
nome3 = str(input('Quarto nome: '))
lista = [nome, nome1, nome2, nome3]
shuffle(lista)
print('A ordem de apresenta~ção será?')
print(lista)
