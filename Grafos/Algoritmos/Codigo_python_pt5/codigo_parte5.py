import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

arq = open('A.txt', 'r') #abre o arquivo no modo read
lista = arq.readlines() #le o arquivo txt e cria uma lista do seu conteudo
lista_final =[]
arq.close()

for x in lista: #esse for le a lista o arquivo e adiciona o seus elementos á outra lista removendo os quebra linhas
    x = x.rstrip('\n')
    lista_final.append(x)

for num in lista_final: #remove os espaços em brancos do final da lista caso tenha algum
    if '' in lista_final:
        lista_final.remove('')

Matriz = [[int(num) for num in line.split(' ')] for line in lista_final] #transforma a lista em uma matriz
A = np.matrix(Matriz)
G = nx.from_numpy_matrix(A)


if nx.is_eulerian(G) == True:
    print("O grafo é Euleriano.")
    x = list(nx.eulerian_circuit(G))
    print(x)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

elif nx.is_eulerian(G) == False:
    print("O grafo não é Euleriano.")
    if nx.has_eulerian_path(G) == True:
        print(list(nx.eulerian_path(G)))
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
    else:
        print("O grafo não possui trilhas Eulerianas.")
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

