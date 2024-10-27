# https://wiki.python.org.br/ExerciciosListas
# exercicio 1: Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 

lista = []

def main():
  for i in range(5):
    entrada = int(input("entre com numero: "))
    print(i + 1 , entrada)
    lista.append(entrada)

  for j in lista:
    print(j)
main()