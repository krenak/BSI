from op_divisors import qtd_divisors
def main():
    n = int(input())
    while n > 0:
        div = qtd_divisors(n)
        print(f"{n} POSSUI {div} DIVISOR" + "ES"*(div>1))
        n = int(input())


if __name__ == "__main__":
    main()