import os
import re
from collections import Counter

folder_path = 'Docs'  

def contador_palavras(ngram, folder_path):
    contador = Counter()
    arquivos = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
          
            with open(file_path, 'r') as file:
                text = file.read()
                text = re.sub(r'[^\w\s]', '', text) #remove pontuação
                sequencia = text.split()
                #aqui verifico se o número de palavras no texto é maior ou igual ao tamanho do n-gram 
                if len(sequencia) >= ngram:
                    for i in range(len(sequencia) - ngram + 1):
                        palavra_final = ' '.join(sequencia[i:i+ngram]) #join() para unir as palavras do n-gram em uma única string
                        contador[palavra_final] += 1
                        #arquivos.append(filename)
    #ngram mais comuns
    return sorted(contador.items(), key=lambda x: x[1])

ngram = 1  #quantidade de palavras para contar
result = contador_palavras(ngram, folder_path)

print("Palavras mais comuns, ordenadas por nível de ocorrência:")
for i, (word, count) in enumerate(result):
    print(f"{word}, {count} ")