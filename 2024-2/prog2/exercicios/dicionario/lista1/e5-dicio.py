'''

prog2 - prof ernani ribeiro

Exercício 4 - Escreva um programa Python que filtre/extraia altura e peso dos
estudantes armazenados em um dicionário de entrada.

ref.: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

def filtroAlunos(d, alt, peso):
    dicioAlunos = {}
    for i in d.keys():
        if d[i][0] > alt and d[i][1] > peso:
            dicioAlunos[i] = d[i]
    return dicioAlunos

def main():
    d = {'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro': (1.72, 66)}
    altura = float(input("digite altura: "))
    peso = float(input("digite peso: "))
    print(d)
    print()
    print(filtroAlunos(d, altura, peso))

main()
