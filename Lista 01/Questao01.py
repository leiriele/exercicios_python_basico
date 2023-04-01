''' Questao02
receba dois numeros inteiros e verifique qual o maior '''

num1 = input("Digite o primeiro número:")
num2 = input("Digite o segundo número:")

# Verificar qual número é o maior e armazena na variavel maior
if num1 > num2:
    maior = num1
    print("O maior número é:", maior)
elif num2 > num1:
    maior = num2
    print("O maior número é:", maior)
else:
    print("Os números informados são iguais!!")
