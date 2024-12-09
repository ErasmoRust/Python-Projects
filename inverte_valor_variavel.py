#troca variável

a=int(input('digite um valor para variavel a : '))
b=int(input('digite um valor para variavel b: '))


if a==b:
    print('O valor da variavel a é igual ao valor da variavel b')
else:
    c = a
    a = b
    b = c
    print (' O novo valor de a eh ',a, 'e o novo valor de b é ', b)