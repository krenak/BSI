'''
lista de exercicios - dicionario
prog2 - pof ernani ribeiro

1. Removedor de acentos
Crie um programa Python que faça uso de dicionario(s) para remover os acentos
de um texto de entrada. Faça o tratamento das maiúsculas e minúsculas. Inclua
o cedilha na lista dos sinais a serem removidos. Construa uma função para a
tarefa principal. Construa uma função main que invoca a função de remoção
dos acentos e exibe, ao final, o texto original e o texto sem acentos.
'''
import palavra as converte

def main():
    p = str(input("palavra a ser convertida: "))
    palavraConvertida = converte.palavra(p)

    print(palavraConvertida)

main()
