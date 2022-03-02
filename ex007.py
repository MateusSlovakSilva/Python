msg = ('Exercício 007 Media do aluno')
print(msg)
nome = str(input('Digite o nome do aluno: '))
nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))
média = (nota + nota2) / 2
print('A média do aluno, {} foi de: {:.1f}'.format(nome, média))