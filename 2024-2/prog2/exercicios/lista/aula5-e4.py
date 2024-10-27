'''
https://wiki.python.org.br/ExerciciosListas
exercicio 4: Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

lista = []
# def consoantes(palavra):
#   return None

def main():
        j = 0
        word = str(input("Entre com a palavra: "))
        for i in word:
                if i.isalpha() and i not in ['a','e','i','o','u']:
                        lista.append(i)
                        j += 1
                print(lista)
        print(f"Foram lidas {j} consoantes, das quais temos")
main()