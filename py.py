from random import randint

lista1 = []
lista2 = []
lista3 = []
lista4 = []

try:
    print(31 * '=')
    print('    MULTIPLICADOR DE MATRIZ')
    print(31 * '=')
    print('Primeiramente você deve criar sua matriz')
    colunas = int(input("Informe o número de colunas:"))
    linha = int(input("Informe o número de linhas:"))
    print('')

    for i in range(0, linha):
        for j in range(0, colunas):
            lista1.append(randint(0,9))
        lista2.append(lista1)
        lista1 = []
        
    for i in range(0, linha):
        for j in range(0, colunas):
            print('{:2}' .format(lista2[i][j]), end='  ')
        print('\b')
    print('')
        
    resposta = int(input("Quer multiplicar a matriz por quanto:"))
    print('')

    for i in range(0,linha):
        for j in range(0, colunas):
            lista3.append(lista2[i][j] * resposta)
        lista4.append(lista3)
        lista3 = []

    print('Resultado da multiplicação:')
    for i in range(0, linha):
        for j in range(0, colunas):
            print('{:2}' .format(lista4[i][j]), end='  ')
        print('\b')
except:
    print('Você digitou algo errado!')
