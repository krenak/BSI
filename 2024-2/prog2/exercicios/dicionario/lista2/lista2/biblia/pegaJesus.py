def arquivo(arquivo):
    arq = open(arquivo, "rt")
    linha = arq.readline()
    palavras = linha.split()
    linhasBiblia = []
    while linha != "":
        linhasBiblia.append(palavras)
        linha = arq.readline()
        palavras = linha.split()
    arq.close()

    return linhasBiblia

def contagem(l):
    cont = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            #sinonimos = ["Jesus", "Cristo", "Senhor", "Salvador", "Messias", "Filho do Homem", "Filho de Deus", "Salvador", "Redentor", "Reis dos Reis", "Palavra de Deus"]
            sinonimos = ["Jesus", "Cristo", "Senhor", "Messias", "Salvador", "Redentor"]
            if l[i][j] in sinonimos:
                cont += 1
            if l[i][j] == "Espírito" and l[i][j + 1] == "Santo":
                cont += 1
            if l[i][j] == "Jesus" and l[i][j + 1] == "Cristo":
                cont += 1
            if l[i][j] == "Filho" and l[i][j + 1] == "de" and l[i][j + 2] == "Deus":
                cont += 1
    return cont

def main():
    linhasBiblia = arquivo("biblia-novo-test.txt")
    contaJesus = contagem(linhasBiblia)
    print("Foram {} vezes que Jesus foi citado.".format(contaJesus))
    # ultimo resultado: 1147 vezes

main()
