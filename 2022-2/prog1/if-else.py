'''
Fazer um programa em Python que leia um número qualquer e imprima uma das
seguintes mensagens: POSITIVO se o número > 0; NULO se o número = 0;
NEGATIVO se o número < 0
'''
# variável de entrada
x = float()
# interface de entrada
x = float(input("Digite um número: "))

#1a solução
# def main()
# if x > 0:
#   print("POSITIVO")
# if x < 0:
#   print("NEGATIVO")
# if x == 0:
#   print("NULO")

# variável de entrada
def main():
    if x != 0:
        if x > 0:
            print("POSITIVO")
        else:
            print("NEGATIVO")
    else:
        print("NULO")
main()
