# funcao princiapl
def main():
    # declaracao de variaveis
    a = int()
    b = int()
    n = int()

    # entrada de dados
    a = int(input())
    b = int(input())
    n = 0

    # main func
    
    if a > 0 and b > 0:
        if a - b >= 0:
            while a - b >= 0:
                a -= b
                n += 1
            
            print(f"QUOCIENTE={n}")
        else:
            print(f"QUOCIENTE=0")            
    else:
        print("ENTRADA INVALIDA")
        
if __name__ == "__main__":
    main()
