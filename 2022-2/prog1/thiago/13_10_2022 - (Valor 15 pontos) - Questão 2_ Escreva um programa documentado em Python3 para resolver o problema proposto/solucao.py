def main():
    n = int(input())
    if n <= 0:
        print(f"N={n} N INVALIDO")
    else:
        s = 0
        for i in range(n):
            aux = (1+i*2)**3
            if i % 2:
                aux *= -1
                print(f"-", end="")
            s += 1/aux
            print(f"1/{1+i*2}^3")
        pi = (s*32)**(1/3)
        print(f"N={n} SOMATORIO={s:.5f} PI={pi:.5f}")
            


if __name__ == "__main__":
    main()