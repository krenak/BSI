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
    for i in nome_arquivo:
        mat = i + "\n"
    pass

def salvaMatriz(m, nome_arquivo):
    if m != None:
        linhas = len(m)
        colunas = len(m[0])
    arquivo = open(nome_arquivo)

def insere(m, l, c, Inserida):
    pass

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
        for i in range((l-1), (l-1) + qtdL):
            lista1 = m[i]
            for j in range(c - 1, (c - 1) + qtdC):
                lista2 = lista1[j]
                novaMatriz.append(lista2)
        return novaMatriz
#                print("%5d" % lista2, " ", end="")
#            print()


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

def formatImpressao2(matriz, l):                    # l = numero de linhas da matriz
    mat = ""
    for numeros in matriz:
        linhas = 1
        while linhas <= l:
            #mat1 = matriz[i]
            mat = mat + " " + str(numeros)
            linhas += 1
        mat = mat + "\n"
    return mat

def formatImpressao(x):
    for z in x:
        for w in z:
            print("%5d" % w, " ", end="")
        print()


# fim das funções
