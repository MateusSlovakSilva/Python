from datetime import date
msg = ('\033[1;4;35mExercício 041\033[m')
print(msg)
atual = date.today().year
nascimento = int(input('Ano de \033[1;32mNascimento: \033[m'))
idade = atual - nascimento
print('O atleta tem \033[4;32m{}\033[m anos.'.format(idade))
if idade <=9:
    print('Atleta \033[1;4;31mMIRIM\033[m')
elif idade <=14:
    print('Atleta \033[1;4;33mINFANTIL\033[m')
elif idade <=19:
    print('Atleta \033[1;4;33mJUNIOR\033[m')
elif idade <=25 :
    print('Atleta \033[1;4;34mSÊNIOR\033[m')
else:
    print('Atleta \033[1;4;32mMASTER\033[m')