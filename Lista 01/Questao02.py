# Questao02
# receba um numero inteiro e verifique se é par ou impar

while True:
    num = int(input("Digite um número inteiro: "))
   # O operador % para calcula o resto da divisão por 2. Se o resto for zero, o número é par
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    # verificar se quer ou nao continuar no loop
    continuar = ""
    # esse while é para verificar se é uma entrada válida
    while continuar not in ['s', 'n']:
        continuar = input("Deseja verificar outro número? (S/N)")
       # caso nao seja uma entrada válida exibe mensagem de erro na tela
        if continuar.lower() not in ['s', 'n']:
            print("Por favor, digite S ou N.")
    # verificar se a entrada é 'n', usamos a expressao break para sair do loop
    if continuar.lower() == "n":
        break
