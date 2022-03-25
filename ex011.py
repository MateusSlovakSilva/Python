msg = ('exercício 011')
print(msg)
largura = float(input('largura da parede: '))
Altura = float  (input('Altura da parede: '))
área = largura * Altura

print('Sua parede tem a dimesão de {} x {} e sua área {}m'.format(largura, Altura, área))
tinta = área /2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))