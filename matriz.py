#Programa multiplicação de duas matriz 3X3
#Crie um programa que declare 2 matrizes de dimensão 3x3 e preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela e apresente o resultado da multiplicação entre as duas matrizes
matriz = [[],[],[]]
matriz2 = [[],[],[]]
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-'*20)
for l in range(0,3):
        for c in range(0,3):
                matriz2[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-'*20)
print('Matriz 1')
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
print('Matriz 2')
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz2[l][c]:^5}]', end='')
        print()
print('-'*20)
#multiplicação das matrizes
for linha in range(0,3):
        for coluna in range(0,3):
          resultado = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matriz2)] for X_row in matriz]
print('Resultado da Multiplicação matriz 3x3')         
for r in resultado:
   print(r)
