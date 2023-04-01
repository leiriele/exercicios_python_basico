''' Questao 04
A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas obedece aos pesos a seguir:
trab1 = peso 2 | trab2 = peso 3 | trab3 = peso 5
receba as três notas, calcule e mostre a média ponderada e o conceito eu segue a tabela
Média ponderada | Conceito
8,01 → 10,0| A
7,01 → 8,0 | B
6,01 → 7,0 | C
5,01 → 6,0 | D
0,00 → 5,0 | E '''
# Receber as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Definir os pesos
peso1 = 2
peso2 = 3
peso3 = 5
# Calcular a media ponderada
media_ponderada = ((nota1*peso1)+(nota2*peso2) +
                   (nota3*peso3))/(peso1+peso2+peso3)
# Verificar se a média ponderada com o conceito correspondente
if media_ponderada >= 8.01 and media_ponderada < 10.0:
    conceito = "A"
elif media_ponderada >= 7.01 and media_ponderada < 8.0:
    conceito = "B"
elif media_ponderada >= 6.01 and media_ponderada < 7.0:
    conceito = "C"
elif media_ponderada >= 5.01 and media_ponderada < 6.0:
    conceito = "D"
else:
    conceito = "E"
# Exibir a média ponderada e o conceito calculados
print("A média ponderada das notas é:", media_ponderada)
print("O conceito correspondente é:", conceito)
