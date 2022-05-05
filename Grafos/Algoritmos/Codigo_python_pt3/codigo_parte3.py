arq = open('C:\\Users\\Gquir\\OneDrive\\Documents - NOTEGUI\\Algoritmos\\Grafos\\Algoritmos\\Codigo_python\\A.txt', 'r') #abre o arquivo no modo read
lista = arq.readlines() #le o arquivo txt e cria uma lista do seu conteudo
lista_final =[]
arq.close()

for x in lista: #esse for le a lista o arquivo e adiciona o seus elementos á outra lista removendo os quebra linhas
    x = x.rstrip('\n')
    lista_final.append(x)
for num in lista_final: #remove os espaços em brancos do final da lista caso tenha algum
    if '' in lista_final:
        lista_final.remove('')
Matriz=[[int(num) for num in line.split(' ')] for line in lista_final] #transforma a lista em uma matriz

def bipartido(matriz):
    result = ""
    Bipartido = True
    u =[]
    v =[]

    def adjacentes(y):
        if len(v) > 1:
            for i in range(len(v)):
                for j in range(len(v)):
                    z = v[i]
                    k = v[j]
                    if matriz[z][k] != 0:
                        return True
        return False

    for i in range(len(matriz)):
        if i not in v:
            u.append(i)
            for j in range(len(matriz)):
                if j > i:
                    if matriz[i][j] > 0:
                        if j not in v:
                            v.append(j)
        if adjacentes(v):
            Bipartido = False

    if Bipartido:
        result+=("O grafo é bipartido, e possui bipartições em u = {")
        for i in range(len(u)):
            if i < len(u)-1:
                result+=("V{}".format(u[i]+1) + ", ")
            else:
                result+=("V{}".format(u[i]+1)+ "} e V = {")

        for j in range(len(v)):
            if j < len(v)-1:
                result+=("V{}".format(v[j] + 1) +", ")
            else:
                result+=("V{}".format(v[j] + 1) + "}")
        result+=("\n")

        def bipartidoCompleto(u, v, matriz):
            resultado = ""
            BipCompleto = True

            for i in range(len(u)):
                cont = 0
                for j in range(len(v)):
                    k = u[i]
                    z = v[j]
                    if matriz[k][z] > 0:
                        cont+=1
                if cont < len(v):
                    BipCompleto = False
                    break

            if BipCompleto:
                resultado+=("O grafo é bipartido completo, pois cada vértice com bipartição em u se conecta a todos os vértices com bipartição em v\n")
            else:
                resultado+=("O grafo não é bipartido completo, pois não são todos os vértices com bipartição em u que se conectam a todos os vértices com bipartição em v\n")
            return resultado

        result+= bipartidoCompleto(u, v, matriz)
        return result

    else:
        return("O grafo não é bipartido, pois possui vértices que se conectam a vértices adjacentes\n")

print(f"\n**************** RESULTADOS *****************\n")
print(bipartido(Matriz))
print(f"*"*80)

