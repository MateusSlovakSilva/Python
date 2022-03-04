msg = ('exercício 008 conversor de medidas')
medida = float(input('Distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print(msg)
print('A medida de {}m corresponde {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))