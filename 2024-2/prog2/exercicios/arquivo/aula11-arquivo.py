'''
E2: Criação de Nomes
Crie 2 listas nos moldes do que foi discutido em aula. A primeira lista, Nomes,
contém 20 dos nomes de pessoas mais frequentes no Brazil. A segunda lista, 
Sobrenomes, possui uma lista dos 15 sobrenomes mais frequentes no Brasil.
Construa uma função que recebe como parâmetros as duas listas e um número
inteiro representando o tamanho do nome da pessoa em partes. Por exemplo, 4:
1 nome + 3 sobrenomes. A função deve retornar um nome de pessoa contendo uma
quantidade de partes definida pelo terceiro parâmetro.

Observação: sem sobrenomes repetidos.

ref:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
'''

def combNomes(nomes, sobren, tam):
    #nomeCompl = []
    for i in nomes:
        for j in range(0, tam):
            novoNome = i + sobren[j]
            print(novoNome)
            #nomeCompl.append(novoNome)
        print()
'''
def processoNomes(n, s, t):
    for i in range(len(t)):                             # iteração da quantidade de partes def pelo 3o parametro
        nome = n[i]                                     # nome de acordo com t[i] 
        sobrenome = ""                                  # var persistente - str()
        for z in range(0, t[i] - 1):                    # iteração dos sobrenomes de acordo com len(t[i])
            sN = random.randint(0, len(s) - 1)          # posição aleatória do sobrenome
            sobrenome1 = s[sN]                          # var auxiliar da concatenação
            sobrenome += " " + sobrenome1               # var str() persistente da concatenação
        nome = nome + sobrenome                         # nome recebe nome + sobrenome
        print(nome)                                     # saída da função processoNomes

    print()
    print("A quantidade de nomes é de:", len(t), "nomes.")
'''

def limpEntrada(n, s, t):

    #sepN = separação da entrada nomes em uma lista de strings
    sepN = str(n.read()) 
    sepN2 = sepN.split(",")

    #sepS = separação da entrada sobrenomes em uma lista de strings
    sepS = str(s.read()) 
    sepS2 = sepS.split("\n")
    
    #sepT = separação da entrada tamanho em uma lista de strings
    sepT = str(t.read()) 
    sepT2 = int(sepT.split("\n"))

    return sepN2, sepS2, sepT2

def main():
    # entradas/abertura de arquivos
    nomes = open("listaNomes.txt", "rt")
    sobrenomes = open("listaSobrenomes.txt", "rt")
    tamanho = open("listaTamanhos.txt", "rt")
    dados = limpEntrada(nomes, sobrenomes, tamanho)

    saida = combNomes(dados[0], dados[1], dados[2])
    print (saida)
    #for i in sepT2:
    #    if 
    #    while i != 0:
            

    ''' If you’re not using the with keyword, then you should call f.close()
        to close the file and immediately free up any system resources used 
        by it.
    '''
    nomes.close()
    tamanho.close()
    sobrenomes.close()

main()

