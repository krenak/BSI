'''
tadPessoas
'''
def load_file(f):
    cadastro = []
    file = open(f, "rt")
    listppl = file.readline().strip()
    while listppl != "":
        person = listppl.split(",")
        cadastro.append(new_pessoas(person[0], int(person[1]), float(person[2]), int(person[3])))
        listppl = file.readline().strip()

    return cadastro

def new_pessoas(n, p, a, i):
    return {"nome": n, "peso": p, "altura": a, "idade": i}

def getNome(tPessoa):
    return tPessoa["nome"]

def getPeso(tPessoa):
    return tPessoa["peso"]

def getAltura(tPessoa):
    return tPessoa["altura"]

def getIdade(tPessoa):
    return tPessoa["idade"]

def maiorIdade(tPessoa):
    return tPessoa["idade"] >= 18

def imc(tPessoa):
    return tPessoa["peso"] / tPessoa["altura"] ** 2

def imcRange(tPessoa):
    status = imc(tPessoa)
    if status < 18.5:
        return "Abaixo do peso ideal"
    elif status <= 24.99:
        return "Peso ideal"
    elif status <= 29.99:
        return "Sobrepeso"
    else:
        return "Obesidade"
