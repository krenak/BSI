'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 19. Escreva um programa Python que verifique se uma dada chave ou um
dado valor existe no dicionário.
Exemplo:
Dicionário de entrada:
[{'id_aluno': 1, 'nome': 'João Castro', 'turma': 'V'}, {'id_aluno': 2, 'nome': 'Lucia Powell',
'turma': 'V'}, {'id_aluno': 3, 'nome': 'Bruno Howell', 'turma': 'VI'}, {'id_aluno': 4, 'nome': 'Luiza
Fonseca', 'turma': 'VI'}, {'id_aluno': 5, 'nome': 'Zacarias Silva', 'turma': 'VII'}]

Saídas para os seguintes chaves/valores:
id_aluno igual a 1 ==> True
nome igual a 'Bruno Howell' ==> True
turma igual a 'VII' ==> True
turma igual a 'I' ==> False
nome igual a 'Bruce Wayne' ==> False
id_aluno igual a 11 ==> False
'''
import pesquisa as pq

def main():
    l = [{'id_aluno': 1, 'nome': 'João Castro', 'turma': 'V'}, {'id_aluno': 2, 'nome': 'Lucia Powell','turma': 'V'}, {'id_aluno': 3, 'nome': 'Bruno Howell', 'turma': 'VI'}, {'id_aluno': 4, 'nome': 'Luiza Fonseca', 'turma': 'VI'}, {'id_aluno': 5, 'nome': 'Zacarias Silva', 'turma': 'VII'}]
    c = int(input("campo a pesquisar (0: id_aluno, 1: nome, 2: turma): "))
    p = input("valor a pesquisar: ")
    c, v, b = pq.pesquisaAlunos(l, c, p)
    pq.imprime(c, v, b)

main()
