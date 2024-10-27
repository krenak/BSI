from calc_primo import eh_primo
def main():
    soma = 0
    prod = 1
    n = int(input())
    while n > 0:
        if eh_primo(n):
            print(f"{n} EH PRIMO")
            soma += n
            prod *= n
        else:
            print(f"{n} NAO EH PRIMO")
        n = int(input())
    print(f"SOMA = {soma}\nPRODUTO = {prod}")

if __name__ == "__main__":
    main()