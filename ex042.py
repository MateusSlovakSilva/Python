msg = ('\033[1;4;35mExercícios 042\033[m')
print(msg)
print('\033[33m-=-\033[m'*9)
print('\033[1;34mAnalisador de Triângulos\033[m')
print('\033[33m-=-\033[m'*9)
primeiro = float(input('\033[33mPrimeiro segmento:\033[m '))
segundo = float(input('\033[33mSegundo segmento:\033[m '))
terceiro = float(input('\033[33mTerceiro segmento:\033[m '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triângulo ', end='')
    if primeiro == segundo == terceiro:  # == igual
        print('\033[1;32mEQUILÁTERO!\033[m')
    elif primeiro != segundo != terceiro !=primeiro: # != diferente 
        print('\033[1;36mESCALENO\033[m')
    else:
        print('\033[1;33mISÓCELES\033[m')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m triângulo!')
    
