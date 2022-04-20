msg = ('\033[1;4;35mExercícios 044\033[m')
print(msg)
preço = float(input('Preço das compras: R$ '))
print(''' \033[1;36mFORMAS DE PAGAMENTO\033[m
\033[1;33m[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m
''')
opçao = int(input('\033[1;32mQual é a opção?\033[m '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em \033[31m2x\033[m de R$ \033[32m{:.2f}\033[m \033[1;32mSEM JUROS\033[m'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('\033[1;33mQuantas parcelas?\033[m '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em \033[32m{}x\033[m de \033[32mR${:.2f}\033[m \033[1;31mCOM JUROS\033[m'.format(totalparcela, parcela))
else:
    total = preço
    print('\033[1;4;31mOPÇÂO INVÁLIDA\033[m de pagamento. \033[1;4;31mTente nova mente!\033[m')
print('Sua compra de R$ \033[32m{:.2f}\033[m vai custar R$ \033[32m{:.2f}\033[m no final.'.format(preço, total))