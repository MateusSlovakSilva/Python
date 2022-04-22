msg = ('\033[1;4;35mExercícios 049\033[m')
print(msg)

num = int(input('\033[1;3;32mQual TABUADA você quer?\033[m '))
for c in range (1, 11):
    print('\033[32m{}\033[m \033[33mX\033[m \033[31m{:2}\033[m = \033[36m{}\033[m'.format(num, c, num*c))
