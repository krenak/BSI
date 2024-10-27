'''
Criação de Nomes

Crie 2 listas nos moldes do que foi discutido em aula. A primeira lista, Nomes, contém 20 dos nomes de pessoas mais frequentes no Brazil. A segunda lista, Sobrenomes, possui uma lista dos 15 sobrenomes mais frequentes no Brasil.
Construa uma função que recebe como parâmetros as duas listas e um número inteiro representando o tamanho do nome da pessoa em partes. Por exemplo, 4: 1 nome + 3 sobrenomes. A função deve retornar um nome de pessoa contendo uma quantidade de partes definida pelo terceiro parâmetro.
Observação: sem sobrenomes repetidos.

ref.: https://docs.python.org/3/library/stdtypes.html#str.split
'''

def sorteio(num):

    return Null


def main():
    #for i in range(20):
    nomes = str(input("Entre com os nomes desejados: "))
    #tam = int(input("Entre com o tamanho do nome desejado: "))
    listaNomes = nomes.split(",")
    
    sobrenomes = str(input("Entre com os sobrenomes desejados: ")) 
    listaSobrenomes = sobrenomes.split(",")
    #listaNomes.append(lista)
    #sobrenomes.split(",")
    #tam.split(",")

    print(listaNomes, listaSobrenomes)

main()


