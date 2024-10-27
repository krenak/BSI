'''
references: https://docs.python.org/3/reference/lexical_analysis.html#identifiers
'''
# equação quadrática - ax(^2)+bx+c=0
print("Esta calculadora auxiliará na resolução de uma equação quadrática.\n"
"Para tal, defina os valores requisitados a seguir:")

def main():
    # declaração de variáveis
    a = float()
    b = float()
    c = float()
    delta = float()
    x1 = float()
    x2 = float()
    
    # variáveis
    a = float(input("Defina o valor de a: "))
    b = float(input("Defina o valor de b: "))
    c = float(input("Defina o valor de c: "))
    
    x1 = float()
    x2 = float()
    
    if a != 0:
        # delta
        delta = b**2-4*a*c
            print("Delta:", delta)
        
        # raízes
        x1 = ((-1*b) + delta**0.5)/(2*a)
        x2 = ((-1*b) - delta**0.5)/(2*a)
        
        # saídas escritas - delta, x', x''
            print("A primeira raiz da equação (x') é:", x1)
            print("A segunda raiz da equação (x'') é:", x2)
        # outras formas de escrever a saída
            #print("delta=%.2f x1=%.2f x2=%.2f" % (delta, x1, x2))
    else:
        print("Valor não divisível")

main()
