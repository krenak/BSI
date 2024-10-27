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

def main():
    # entradas/abertura de arquivos
    nomes = ["Ana", "Maria", "Juliana", "Fernanda", "Aline", "Patricia", "Beatriz", "Camila", "Larissa", "Letícia", "João", "Pedro", "Lucas", "Gabriel", "Rafael", "Thiago", "Matheus", "Felipe", "Bruno", "Leonardo"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Ferreira", "Souza", "Almeida", "Costa", "Lima", "Pereira", "Rocha", "Martins", "Gomes", "Ribeiro", "Alves", "Nascimento", "Vieira", "Martins", "Barros", "Cardoso", "Mendes"]
    tamanho = [3, 7, 1, 5, 9, 2, 4, 6, 8, 10, 3, 7, 2, 6, 1, 8, 5, 4, 9, 10] 
    # chamada de função para processar os nomes e sobrenomes de acordo com o tamanho
    dados = processoNomes(nomes, sobrenomes, tamanho)

main()

