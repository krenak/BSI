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
https://docs.python.org/3/library/random.html#random.randint
https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting
https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
'''

import random                                           # random.randint(x, y) para sequencia aleatoria de inteiros

def processoNomes(n, s, t):
    nomeCompleto = []                                   # lista vazia de lista de nomes
    for i in range(len(t)):                             # iteração da quantidade de partes def pelo 3o parametro
        nome = n[i]                                     # nome de acordo com t[i] 
        sobrenome = []                                  # lista vazia de sobrenomes
        snC = 0                                         # contador de comparação de sobrenomes
        while snC != (t[i] - 1):                        # looping para completar o sobrenome sem repetição de termos
            sN = random.randint(0, len(s) - 1)          # posição aleatória do sobrenome
            sobrenome1 = s[sN]                          # var auxiliar da concatenação
            if sobrenome1 not in sobrenome:             # teste lógico de checagem de repetição de termos
                sobrenome.append(sobrenome1)            # append na lista sobrenomes
                snC += 1
        for j in range(len(sobrenome)):
            nome = nome + " " + sobrenome[j]            # nome recebe nome + sobrenome
        nomeCompleto.append(nome)
    return nomeCompleto                                 # saída da função processoNomes

# início da função main
def main():
    # entradas/abertura de arquivos
    nomes = ["Ana", "Maria", "Juliana", "Fernanda", "Aline", "Patricia", "Beatriz", "Camila", "Larissa", "Letícia", "João", "Pedro", "Lucas", "Gabriel", "Rafael", "Thiago", "Matheus", "Felipe", "Bruno", "Leonardo"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Ferreira", "Souza", "Almeida", "Costa", "Lima", "Pereira", "Rocha", "Martins", "Gomes", "Ribeiro", "Alves", "Nascimento", "Vieira", "Martins", "Barros", "Cardoso", "Mendes"]
    tamanho = [3, 7, 1, 5, 9, 2, 4, 6, 8, 10, 3, 7, 2, 6, 1, 8, 5, 4, 9, 10] 
    # chamada de função para processar os nomes e sobrenomes de acordo com o tamanho
    dados = processoNomes(nomes, sobrenomes, tamanho)

    for i in dados:
        print(i)
main()
# fim da função main
