#Criando e manipulando um array
#Autor Leiriele Correa

import array as arr

# criando um array do tipo inteiro (i -> define o tipo)
a = arr.array('i', [1, 2, 3, 4])
print("Array original", a)

print("Inserir elementos no array existente")
#adicionar um elemento ao array
a.append(5)
print("Array usando append: ",a)
#adicionar uma lista de elementos ao array
a.extend([6, 7, 8, 9])
print("Array usando extend: ",a)	

#Acessando elementos do array
print("Acessando elementos do array")
#Primeiro elemento
print("Primeiro elemento do array:", a[0])
#Segundo elemento
print("Segundo elemento do array:", a[1])
#Ultimo elemento
print("Ultimo elemento do array:", a[-1])

#Concatenar Array  
b = arr.array('i', [1, 3, 5])
c = arr.array('i', [2, 4, 6])
concatenar = arr.array('i')   # criando um array vazio de inteiro
concatenar = b + c
print("Array 1: ",b)
print("Array 2: ",c)
print("Concatenando array 1 + array 2: ", concatenar) 

#Remover elemento do array
print("Array original:",a)
#Remove remove o item fornecido
a.remove(2)
print("Array depois:",a)
#POP remove um item no índice fornecido
a.pop(4)
print("Array depois do pop:",a)