# funcao princiapl
def main():
    # declaracao de variaveis
    a = int()
    b = int()
    c = int()
    maior = int()
    texto1 = str()
    texto2 = str()
    texto2 = ""

    # entrada de dados
    a  = int(input())
    b  = int(input())
    c  = int(input())

    # main func
    while not (a == 0 and b == 0 and c == 0):
        if a == b and b == c:
            maior = a
        elif a>=b and a>=c:
            maior = a
        elif b>=a and b>=c:
            maior = b
        else:
            maior = c

        texto1 = f"MAIOR({a},{b},{c}) = {maior}\n"
        texto2 = f"{texto2}{texto1}"        
        a = int(input())
        b = int(input())
        c = int(input())
    print(texto2[0:len(texto2)])

if __name__ == "__main__":
    main()
