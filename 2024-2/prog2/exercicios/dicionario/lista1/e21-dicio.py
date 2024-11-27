'''
lista de exercicios - dicionario
prog2 - prof ernani ribeiro

Exercicio 21. Escreva um programa Python que receba um arquivo texto de entrada
e retorne um dicionário com pares chave:valor do tipo
'tamanho da palavra':'lista de palavras com este tamanho'.

Exemplo:
Texto de entrada: "Hoje é um bom dia para a escrita de códigos"

Dicionário de saída:
{1:['é','a'],4:['Hoje','para'],2:['um','de'],3:['bom','dia'],7:['escrita','códigos']}
'''
import tamanho as tam

def main():
    entrada = tam.abrirArquivo("textoEntrada.txt")
    d = tam.tamanhoPalavras(entrada)
    print(d)

main()
