'''
lista de exercicios - dicionario
prog2 - ernani ribeiro

Exercicio 3.- Escreva um programa Python que converta listas de entrada em uma
lista de dicionários aninhados. O exemplo a seguir ilustra o problema para 3
listas de entrada.

ref.: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

def dicioAninhados(l1, l2, l3):
    listaEnderecos = []
    dicioEndereco = {}
    for i in range(len(l1)):
        dicioEndereco = {l1[i]:{l2[i]:l3[i]}}
        listaEnderecos.append(dicioEndereco)
    return listaEnderecos

def main():
    ent1 = ['S001', 'S002', 'S003', 'S004']
    ent2 = ['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
    ent3 = [85, 98, 89, 92]
    print(ent1, ent2, ent3)
    saida = dicioAninhados(ent1, ent2, ent3)
    print()
    print(saida)

main()
