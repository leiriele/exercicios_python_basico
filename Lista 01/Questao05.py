''' Faça um algoritmo que receba quatro valores: I, A, B e C. Desses valores, I éinteiro positivo, A, B e C são reais.
 Escreva os números A, B e C obedecendo à tabela a seguir:
 Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3 e que os números digitados sejam diferentes um do outro
 Valor de I | Forma de Escrever
 1 | A, B e C em ordem crescente
 2 | A, B e C em ordem decrescente
 3 | O maior fica entre os outros dois números'''

I = int(input("Digite o valor de I [1, 2 ou 3]: "))
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Verificando se os valores de A, B e C são diferentes um do outro
if A == B or A == C or B == C:
    print("Os valores de A, B e C precisam ser diferentes um do outro.")
else:
    # Verificando o valor de I e imprimindo os valores de A, B e C de acordo com a tabela
   #verificando qual é o menor valor entre A, B e C, e imprimindo-os em ordem crescente.
    if I == 1:
        if A < B and A < C:
            if B < C:
                print(A, B, C)
            else:
                print(A, C, B)
        elif B < A and B < C:
            if A < C:
                print(B, A, C)
            else:
                print(B, C, A)
        else:
            if A < B:
                print(C, A, B)
            else:
                print(C, B, A)
   # ordem decrescente.
    elif I == 2:
        if A > B and A > C:
            if B > C:
                print(A, B, C)
            else:
                print(A, C, B)
        elif B > A and B > C:
            if A > C:
                print(B, A, C)
            else:
                print(B, C, A)
        else:
            if A > B:
                print(C, A, B)
            else:
                print(C, B, A)
    #imprimi os valores de A, B e C de modo que o maior valor fique entre os outros dois
    elif I == 3:
        if A > B and A > C:
            if B > C:
                print(B, A, C)
            else:
                print(C, A, B)
        elif B > A and B > C:
            if A > C:
                print(A, B, C)
            else:
                print(C, B, A)
        else:
            if A > B:
                print(A, C, B)
            else:
                print(B, C, A)
    else:
        print("O valor de I precisa ser 1, 2 ou 3.")
