'''
3. Matrizes
Crie um arquivo em Python chamado libmatriz.py. Neste arquivo, crie 2 funções:
loadMatriz(nome_arquivo) e salvaMatriz(mat, nome_arquivo). A função loadMatriz
deve processar o arquivo de nome nome_arquivo carregando o seu conteúdo e 
retornando-o como uma matriz. A função salvaMatriz deve salvar a matriz mat 
em um arquivo de nome nome_arquivo.

Observação: Todos os arquivos de matrizes, para leitura ou para escrita, devem 
estar organizados no formato de matrizes, cada linha do arquivo é uma linha da 
matriz com os respectivos elementos separados por espaço.

Utilizando as funções loadMatriz(..) e salvaMatriz(..), crie as funções mostradas 
nas figuras 1 e 2 a seguir. Armazene essas funções no arquivo libmatriz.py. Teste 
cada uma das funções criando uma aplicação de testes.
'''

import random

def loadMatriz(nome_arquivo):
    arquivo = open(nome_arquivo, "rt")
    lista = arquivo.readline()
    matriz = []
    matrizInt = []
    while lista != "\n":
        l1 = lista.split()
        matriz.append(l1)
        lista = arquivo.readline()

    linha = []
    for itens in matriz:
        for j in itens:
            linha.append(int(j))
        matrizInt.append(linha)
        linha = []
    arquivo.close()

    return matrizInt


def salvaMatriz(m, nome_arquivo):
    if m != None:
        linhas = len(m)
        colunas = len(m[0])
        matriz = ""
        matrizFinal = ""
        for l in range(linhas):
            for c in range(colunas):
                matriz = matriz + str(m[l][c]) + " "
            matrizFinal = matrizFinal + matriz + "\n"
            matriz = ""
    
    arquivo = open(nome_arquivo, "wt")
    arquivo.write(matrizFinal)

    arquivo.close()

def insere(m, l, c, inserida):
    # definindo a matriz menor a ser inserida
    qtdL = int(input("qtd de linhas a inserir: "))
    qtdC = int(input("qtd de colunas a inserir: "))
    matInserida = []
    linhaMat = []
    for linhas in range(qtdL):
        for colunas in range(qtdC):
            linhaMat.append(inserida)
        matInserida.append(linhaMat)
        linhaMat = []

    # recriando a matriz com a matriz menor inserida
    novaMatriz = []
    for i in range(len(m)):
        # condição onde a linha matriz princip é igual a linha de inserir matriz
        if i >= l and i <= qtdL:
            # início da matriz principal
            for j in range(0, c):
                linhaMat.append(m[i][j])
            
            # ponto inicial (coluna) onde insere matriz menor
            pos = 0 # posição da linha da matriz menor
            for k in range(qtdC):
                linhaMat.append(matInserida[pos][k])
                pos += 1

            # fim da matriz principal
            for z in range(c + qtdC, len(m)):
                linhaMat.append(m[i][z])
            novaMatriz.append(linhaMat)
        else:
            novaMatriz.append(m[i])
        linhaMat = []

    return novaMatriz

#        for linhaInsere in range(l, l + qtdL):
#            linha.append(matInserida[linhaInsere])
#            print(linha)
#    return matInserida

def testeLogico(m, x, y, qtdC, qtdL): # sugestao do Ernani
    qL = len(m)
    qC = len(m[0])
    if (x < 0) or (x > qL):
        return None
    elif (y < 0) or (y > qC):
        return None
    elif qtdL <= 0:
        return None
    elif qtdC <= 0:
        return None
    else:
        return True

def extraiMat(m, l, c, qtdL, qtdC):
    tt = testeLogico(m, l, c, qtdL, qtdC)
    if tt == True:
        novaMatriz = []
        novaLinha = []
        for i in range(l, l + qtdL):
            lista1 = m[i]
            for j in range(c, c + qtdC):
                novaLinha.append(lista1[j])
            novaMatriz.append(novaLinha)
            novaLinha = []
        return novaMatriz

def geraMat(lin, col, minimo, maximo):
    matriz = []
    for i in range(lin):
        matrizLinhas = []
        for j in range(col):
            # caso o valor minimo seja trocado com o maximo e vice-versa
            if minimo > maximo:
                aux = minimo
                minimo = maximo
                maximo = aux
                elem = random.randint(minimo, maximo)
            else:
                elem = random.randint(minimo, maximo)
            matrizLinhas.append(elem)
        matriz.append(matrizLinhas)
    return matriz

def formatImpressao(matriz):
    for linhas in matriz:
        for colunas in linhas:
            print("%1d" % colunas, " ", end="")
        print()

#def formatImpressao2(matriz, lin, col):                    # l = numero de linhas da matriz
#    mat = ""
#    #linhas = int(len(matriz)/col)
#    novaLinha = 0
#    for i in range(0, lin - 1):
#        #mat1 = matriz[i]
#        mat = mat + " " + str(matriz[i])
#        if novaLinha == col:
#            mat = mat + "\n"
#            novaLinha = 0
#        novaLinha += 1
#    return mat

# fim das funções
