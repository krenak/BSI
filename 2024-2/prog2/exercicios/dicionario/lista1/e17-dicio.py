'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 17.Escreva um programa Python que extraia os valores de dicionários
presentes em uma lista e retorne uma lista de listas com esses valores.

Exemplo:
Dicionário de entrada:
[{'id_aluno': 1, 'nome': 'João Castro', 'turma': 'V'}, {'id_aluno': 2, 'nome': 'Lucia Powell','turma': 'V'}, {'id_aluno': 3, 'nome': 'Bruno Howell', 'turma': 'VI'}, {'id_aluno': 4, 'nome': 'Luiza Fonseca', 'turma': 'VI'}, {'id_aluno': 5, 'nome': 'Zacarias Silva', 'turma': 'VII'}]

Lista de lista dos valores de cada dicionário de entrada:
[[1, 'João Castro', 'V'], [2, 'Lucia Powell', 'V'], [3, 'Bruno Howell', 'VI'], [4, 'Luiza Fonseca',
'VI'], [5, 'Zacarias Silva', 'VII']]
[[1, 'João Castro'], [2, 'Lucia Powell'], [3, 'Bruno Howell'], [4, 'Luiza Fonseca'], [5, 'Zacarias
Silva']]
[['João Castro', 'V'], ['Lucia Powell', 'V'], ['Bruno Howell', 'VI'], ['Luiza Fonseca', 'VI'],
['Zacarias Silva', 'VII']]
'''
import combinacoes as comb

def main():
    l = [{'id_aluno': 1, 'nome': 'João Castro', 'turma': 'V'}, {'id_aluno': 2, 'nome': 'Lucia Powell','turma': 'V'}, {'id_aluno': 3, 'nome': 'Bruno Howell', 'turma': 'VI'}, {'id_aluno': 4, 'nome': 'Luiza Fonseca', 'turma': 'VI'}, {'id_aluno': 5, 'nome': 'Zacarias Silva', 'turma': 'VII'}]
    print(l)
    print()
    combinacoes = comb.combinaListas(l)
    comb.imprime(combinacoes)
main()
