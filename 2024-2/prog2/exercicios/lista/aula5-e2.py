# https://wiki.python.org.br/ExerciciosListas
# exercicio 2: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

def main():
  for i in range(10):
    entrada = float(input("entre com numero: "))
    print(i + 1 , entrada)
    lista.append(entrada)

  for j in range(len(lista)-1, -1, -1):
    print(lista[j])
main()