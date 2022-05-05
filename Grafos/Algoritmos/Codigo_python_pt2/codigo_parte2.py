arq = open('C:\\Users\\Gquir\\OneDrive\\Documents - NOTEGUI\\Algoritmos\\Grafos\\Algoritmos\\Codigo_python\\A.txt', 'r') ## Abre o arquivo no modo "read" ##
lista = arq.readlines() ## Lê o arquivo ".txt" e cria uma lista com seu conteúdo ##
lista_final =[]
arq.close()

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
