'''
código em python sobre o método de compressão sem perdas de dados do código de
Huffman

linha 63 ---> 1) Defina o número de caracteres máximos que há no texto (50.000)

linha 17 ---> 2) usuário define um texto

pendente, mas acho que não precisa dele definir não ---> 3) o usuáriro atribui 
um valor probabilistico para ocorrencia de cada letra diferente (letras iguais 
repetem a probabilidade) e a somatória precisa ser igual a 100%

WIP na linha 56 ---> 4) as letras são lidas e organizadas em filas em ordem 
crescente numérica

WIP na linha 56 ---> 5) Construir a árvore de Huffman

pendente ---> 6) Construir a tabela de codificação para cada caractere e seu 
respectivo valor binário

pendente ---> 7) Codificar a palavra que foi definida

pendente ---> 8) Multiplicar por 8 o valor inserido no primeiro ponto, ou seja,
o número de caracteres máximos que há no texto

pendente ---> 9) retornar quantos bits são necessário para armazenar o texto 
usando a codificação de Huffman
'''

def quantidade_caracteres():
    pass

# funcao que carrega o arquivo texto a ser comprimido
def carregaTexto(arquivo):
    conteudo = []
    arquivo = open(arquivo, "rt", encoding="utf-8")
    linhas = arquivo.readline().strip()
    while linhas != "":
        linhasTexto = linhas.split()
        conteudo.append(linhasTexto)
        linhas = arquivo.readline().strip()
    arquivo.close()

    return conteudo

# funcao que quantas vezes cada caractere aparece no texto fornecido
def contador(texto):
    dicioLetras = {}
    for linhas in texto:
        for palavras in linhas:
            cont = 1
            for letras in palavras:
                if letras not in dicioLetras:
                    dicioLetras[letras] = {"cont": cont}
                else:
                    cont += 1
                    dicioLetras[letras] = {"cont": cont}

    return dicioLetras

# funcao que calcula a proporcao que os caracteres aparecem no texto fornecido
def freqCaracteres(d):
    totalCaracteres = int(len(d.keys())) + 1 # quantidade total/maxima de caracteres
    freqC = {}
    for letra in d.keys():
        freq = (int(d[letra]["cont"]) / totalCaracteres) * 100
        freqC[letra] = {"frequencia": freq, "peso": 0}

    return freqC

# funcao que recebe e ordena o dicionario com os símbolos e suas
# respec. frequencias
def arvore(d):
    listaSimbol = []
    menorValor = -1
    for freq in d.keys():
        freqSimbol = d[freq]['frequencia']
        # ordenando as frequencias para atribuir peso a elas
        if freqSimbol < menorValor:
            menorValor = freqSimbol
            listaSimbol.append(d[frequencia])


def main():
    # funcao de abrir o arquivo de texto, em txt
    texto = carregaTexto("teste2.txt")
    # funcao contagem de caracteres e símbolos para o texto
    contagem = contador(texto)
    freq = freqCaracteres(contagem)
    arvoreBinaria = arvore(freq)
    for letras in freq.keys():
        print("Frequência de {:s}: {:.2f}%".format(letras, freq[letras]["frequencia"]))
    print(arvoreBinaria)


main()

'''
import heapq
from collections import defaultdict, Counter

# Passo 1: Contar frequências
def calculate_frequencies(text):
    return Counter(text)

# Passo 2: Construir a árvore de Huffman
def build_huffman_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Passo 3: Gerar o código de Huffman
def huffman_encoding(text):
    frequencies = calculate_frequencies(text)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_code = {char: code for char, code in huffman_tree}
    encoded_text = ''.join(huffman_code[char] for char in text)
    return encoded_text, huffman_code

# Passo 3.1: Calcular o numero de bits para armazenar o texto codificado
def calculate_encoded_size(text, huffman_code):

    # Contar a frequência de cada caractere no texto
    frequencies = calculate_frequencies(text)

    # Calcular o tamanho total em bits
    total_bits = sum(frequencies[char] * len(huffman_code[char]) for char in frequencies)

    return total_bits

# Passo 3.2: Calcula o número total de bits necessários para armazenar o texto usando ASCII.


def calculate_ascii_size(text):

    return len(text) * 8


# Passo 4: Decodificar o texto (opcional)
def huffman_decoding(encoded_text, huffman_code):
    reverse_code = {code: char for char, code in huffman_code.items()}
    decoded_text = ""
    temp = ""
    for bit in encoded_text:
        temp += bit
        if temp in reverse_code:
            decoded_text += reverse_code[temp]
            temp = ""
    return decoded_text


# Exemplo de uso
if __name__ == "__main__":
    text = "ANDERSON"

    # Codificação
    encoded_text, huffman_code = huffman_encoding(text)
    print("Texto original:", text)
    print("Texto codificado:", encoded_text)
    print("Códigos de Huffman:", huffman_code)

    # Calcular o número de bits necessários com Huffman
    total_bits_huffman = calculate_encoded_size(text, huffman_code)
    print("Número total de bits necessários para armazenar o texto codificado (Huffman):", total_bits_huffman)

    # Calcular o número de bits necessários com ASCII
    total_bits_ascii = calculate_ascii_size(text)
    print("Número total de bits necessários para armazenar o texto codificado (ASCII):", total_bits_ascii)

    # Decodificação
    decoded_text = huffman_decoding(encoded_text, huffman_code)
    print("Texto decodificado:", decoded_text)
'''
