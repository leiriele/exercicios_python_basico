''' Questao 03
 receba três números obrigatoriamente em ordem crescente e um quarto numero que não siga essa regra.
 Mostre, em seguida, os quatro números em ordem decrescente.
 Suponha que o usuário digitará quatro números diferentes. '''

num1 = int(input("Digite o primeiro número: "))
# Esse loop é para verficar se o segundo numero é maior que o primeiro, senao exibe msg de erro
while True:
    num2 = int(input("Digite o segundo número: "))
    if num2 > num1:
        break
    print("O número informado deve ser maior que o primeiro!")
# Esse loop é para verficar se o terceiro numero é maior que o segundo, senao exibe msg de erro
while True:
    num3 = int(input("Digite o terceiro número: "))
    if num3 > num2:
        break
    print("O número informado deve ser maior que o primeiro!")
    # Agora solicito o quarto numero
num4 = int(input("Digite o quarto numero: "))
# Verificar se o quarto numero é maior que os anteriores. 'aux' indicará quantas mudanças foram feitas
# Se o quarto número é maior que o terceiro, mover os outros números
if num4 > num3:
    aux = 1
# Se o quarto número é maior que o segundo, mas não é maior que o terceiro, então precisamos mover o terceiro número para a quarta posição e colocar o quarto número na terceira posição
elif num4 > num2:
    num3, num4 = num4, num3
    aux = 2
# Se o quarto número é maior que o primeiro, mas não é maior que o segundo ou o terceiro, então precisamos mover o segundo número para a terceira posição, o terceiro número para a quarta posição e colocar o quarto número na segunda posição
elif num4 > num1:
    num2, num3, num4 = num4, num3, num2
    aux = 3
# Se o quarto número não é maior que nenhum dos três primeiros, então precisamos mover o primeiro número para a segunda posição, o segundo número para a terceira posição, o terceiro número para a quarta posição e colocar o quarto número na primeira posição
else:
    num1, num2, num3, num4 = num4, num1, num2, num3
    aux = 4
# Resultado em ordem decrescente
print("Os quatro números em ordem decrescente:")
if aux == 1:
    print(num4, num3, num2, num1)
elif aux == 2:
    print(num3, num4, num2, num1)
elif aux == 3:
    print(num3, num2, num4, num1)
else:
    print(num3, num2, num1, num4)
