msg = ('Exercícios 031')
print(msg)
distancia = float(input('Qual é a distancia da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Eo preço da sua passagem será de R${:.2f}'.format(preço))
