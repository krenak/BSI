def quantidade_caracteres(texto):
    frequencia = {}
    for linha in texto:
        for palavra in linha:
            for caractere in palavra:
                if caractere not in frequencia:
                    frequencia[caractere] = 0
                frequencia[caractere] += 1
    return frequencia

def carregaTexto(arquivo):
    conteudo = []
    with open(arquivo, "rt", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linhasTexto = linha.strip().split()
            conteudo.append(linhasTexto)
    return conteudo

def contador(texto):
    return quantidade_caracteres(texto)

def freqCaracteres(d):
    totalCaracteres = sum(d.values())
    freqC = {}
    for letra, cont in d.items():
        freq = (cont / totalCaracteres) * 100
        freqC[letra] = {"frequencia": freq, "peso": 0}
    return freqC

def construir_arvore_huffman(frequencias):
    nos = [(freq["frequencia"], i, (char, None, None)) for i, (char, freq) in enumerate(frequencias.items())]
    
    while len(nos) > 1:
        nos.sort(key=lambda x: (x[0], x[1]))
        (freq1, _, esquerda), (freq2, _, direita) = nos.pop(0), nos.pop(0)
        novo_no = (freq1 + freq2, len(nos), (None, esquerda, direita))
        nos.append(novo_no)
    
    return nos[0][2]

def gerar_codigos(no, codigo_atual="", codigos=None):
    if codigos is None:
        codigos = {}

    if no[1] is None and no[2] is None:  # é uma folha
        codigos[no[0]] = codigo_atual
        return codigos

    codigos = gerar_codigos(no[1], codigo_atual + "0", codigos)
    codigos = gerar_codigos(no[2], codigo_atual + "1", codigos)

    return codigos

def comprimir(texto, codigos):
    texto_comprimido = ""
    for linha in texto:
        for palavra in linha:
            for caractere in palavra:
                texto_comprimido += codigos[caractere]
    return texto_comprimido

def main():
    texto = carregaTexto("teste2.txt")
    contagem = contador(texto)
    freq = freqCaracteres(contagem)
    
    arvore = construir_arvore_huffman(freq)
    codigos = gerar_codigos(arvore)
    
    print("Frequências:")
    for letra, info in freq.items():
        print(f"Frequência de {letra}: {info['frequencia']:.2f}%")
    
    print("\nCódigos Huffman:")
    for caractere, codigo in codigos.items():
        print(f"{caractere}: {codigo}")
    
    texto_comprimido = comprimir(texto, codigos)
    print(f"\nTexto comprimido: {texto_comprimido}")

    taxa_compressao = (len(texto_comprimido) / (len(str(texto)) * 8)) * 100
    print(f"\nTaxa de compressão: {taxa_compressao:.2f}%")

main()
