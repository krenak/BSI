# Arquivo com as definições das funções (mod_atividade_10.py)

# Função de cálculo do mdc

import mod_atividade10

def main():
    # declaracao de variaveis
    n = int()
    m = int()
    p = int()
    z = int() # variavel intermediaria
    # inicializacao de variaveis
    flag = 0
    # processamento de dados
    while not flag == 25:
        # entrada de dados
        n = int(input())
        m = int(input())
        p = int(input())
        # chamada de funcoes
        z = mod_atividade10.mdc_euclides(n,m)
        mdc = mod_atividade10.mdc_euclides(z,p)
        print(f"MDC({n}, {m}, {p})={mdc}")
        flag += 1
    #fim da função main
#invocação/chamada do programa principal
if __name__ == "__main__":
  main()
#fim
