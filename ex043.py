msg = ('\033[1;4;35mExercícios 043\033[m')
print(msg)
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura ** 2) # ** eleva o numero
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc <25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')  
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
    