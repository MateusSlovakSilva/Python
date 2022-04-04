import emoji
msg = ('\033[1;4;35mExercícios 035\033[m')
print(msg)
num = int(input('\033[1;31mDigite um número inteiro:\033[m '))
print(emoji.emojize('''\033[4;36mEscolha uma das bases para conversão:\033[m 
\033[33m[ 1 ] Converter para BINÁRIO:thinking:
[ 2 ] Convcerter para OCTAL:thinking:
[ 3 ] Converter para HEXADECIMAL :thinking:''',language='alias'))
opção = int(input('\033[1;31mSua opção:\033[m'))
if opção == 1:
    print(emoji.emojize('\033[32m{}\033[m convertido para \033[1;32mBINÁRIO\033[m é igual a \033[32m{}\033[m :open_mouth:'.format(num, bin(num) [2:]),language='alias'))
elif opção == 2:
    print(emoji.emojize('\033[32m{}\033[m convertido para \033[1;32mOCTAL\033[m é igual a \033[32m{}\033[m :open_mouth:'.format(num, oct(num) [2:]),language='alias'))
elif opção == 3:
    print(emoji.emojize('\033[32m{}\033[m convertido para \033[1;32[mHEXADECIMAL\033[m é igual a \033[32m{}\033[m :open_mouth:'.format(num, hex(num)[2:]),language='alias'))
else:
    print(emoji.emojize('\033[1;31mOpoção invalida tente novamente!\033[m :expressionless:',language='alias'))
