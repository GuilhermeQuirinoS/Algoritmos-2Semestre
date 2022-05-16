arq = open('A.txt', 'r')
lista = arq.readlines()
lista_final =[]
arq.close()

def simples():
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

def regular():
    for x in lista: ## Esse "for" lê a lista e o arquivo e adiciona o seus elementos a outra lista, removendo as quebras de linhas ##
        x = x.rstrip('\n')
        lista_final.append(x)
    for num in lista_final: ## Remove os espaços em branco do final da lista, caso tenha algum ##
        if '' in lista_final:
            lista_final.remove('')

    Matriz=[[int(num) for num in line.split(' ')] for line in lista_final] ## Transforma a lista em uma matriz ##
    Matriz2 = [[int(num) for num in line.split(' ')] for line in lista_final]

    ## Faz a Sequência dos graus ##
    arestas = 0
    grau = []

    ## Faz a Sequência dos graus ##
    for linha in range(len(Matriz2)):
        for coluna in range(len(Matriz2[linha])):
            if coluna == linha and Matriz2[linha][coluna]>= 1:
                Matriz2[linha][coluna] = Matriz2[linha][coluna]*2
    for linha in Matriz2:
        grau.append(sum(linha))

    ## Conta o número de arestas ##
    for linha in range(len(Matriz2)):
        for coluna in range(len(Matriz2[linha])):
            arestas = arestas + Matriz2[linha][coluna]

    print(f"\n**************** RESULTADOS *****************\n")
    print(f"* O grafo possui",int(arestas/2),"arestas\n")

    ## Verifica se o grafo é completo ##
    aresta_multipla = 0
    laco = 0

    for linha in range(len(Matriz)):
        for coluna in range(len(Matriz[linha])):
            if linha == coluna and Matriz[linha][coluna] > 0:
                laco = laco + Matriz[linha][coluna]
            if Matriz[linha][coluna] > 1 and linha != coluna:
                aresta_multipla = aresta_multipla + 1

    ## Verifica se o grafo possui laços ou arestas múltiplas ##
    if laco > 0 or aresta_multipla > 1:
        print(f"* O grafo não é completo!\n")
    elif laco == 0 and aresta_multipla == 0:
        verifica = 0
        ant = 0
        pro = 0
        for x in grau:
            pro = x
            if x == ant:
                verifica = 1

            else:
                ant = pro
                verifica = 0

        if verifica == 0:
            print(f"* O grafo não é completo!\n")
        elif verifica == 1:

            print(f"* O grafo é completo!\n")


    ## Verifica se o grafo é regular ##
    verifica2 = 0
    ant = 0
    pro = 0
    for x in grau:
        pro = x
        if x == ant:
            verifica2 = 1

        else:
            ant = pro
            verifica2 = 0

    if verifica2 == 0:
        print(f"* O grafo não é regular!\n")
    elif verifica2 == 1:

        print(f"* O grafo é regular!\n")

    ## Coloca a sequência dos graus em ordem decrescente ##
    grau.sort(reverse=True)

    print(f"* Sequência de graus do grafo = {grau}")

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
simples()
regular()
print(f"*"*46)