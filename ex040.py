msg = ('\033[1;4;34mMédia\033[m')
print(msg)
n = float(input('\033[33mDigite a primeira nota:\033[m '))
n1 = float(input('\033[33mDigite a sehunda nota:\033[m '))
total = (n + n1) / 2
if total >=90 and total < 100:    
    print('\033[1;4;34mMÉDIA A\033[m')
elif total >=80 and total <90:
    print('\033[1;4;32mMÉDIA B\033[m')
elif total >=70 and total <80:
        print('\033[1;4;33mMÉDIA C\033[m')
elif total >=60 and total <70:
    print('\033[1;4;31mMÉDIA D\033[m')
    print('Está de \033[1;31mRECUPERAÇÃO\033[m')    
else:
    total >=50 and total <50
    print('\033[1;4;31mMÉDIA E\033[m')
    print('Está de \033[1;31mRECUPERAÇÃO\033[m')
print('A somas das notas \033[32m{}\033[m e \033[032m{}\033[m deu a soma \033[1;4;32m{}\033[m'.format(n, n1, total))
