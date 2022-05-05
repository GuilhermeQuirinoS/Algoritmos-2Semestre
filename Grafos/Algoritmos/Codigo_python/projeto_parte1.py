arq = open('C:\\Users\\Gquir\\OneDrive\\Documents - NOTEGUI\\Algoritmos\\Grafos\\Algoritmos\\Codigo_python\\A.txt', 'r')
lista = arq.readlines()
lista_final =[]
arq.close()

for x in lista:
    x = x.rstrip('\n')
    lista_final.append(x)

for num in lista_final:
    if '' in lista_final:
        lista_final.remove('')

Matriz = [[int(num) for num in line.split(' ')] for line in lista_final]
aresta = 0
laco = 0

for linha in range(len(Matriz)):
    for coluna in range(len(Matriz[linha])):
        if linha == coluna and Matriz[linha][coluna] > 0:
            print(f"Laço encontrado no vértice V{linha+1}\n")
            laco = laco + Matriz[linha][coluna]
for linha in range(len(Matriz)):
    for coluna in range(len(Matriz[linha])):
        if Matriz[linha][coluna] > 1 and linha != coluna:
            print(f"Aresta múltipla encontrada entre os vértices V{linha+1} e V{coluna+1}\n")
            aresta = aresta + 1

if laco > 0 or aresta > 1:
    print(f"O grafo não é simples porque possui {laco} laço(s) e {int(aresta/2)} arestas múltiplas.\n")
else:
    print("O grafo é simples porque não possui laços nem arestas múltiplas\n")
