from mod import get_sqrt
def main():
    n = int(input())
    while n > 0:
        prec = int(input())
        print(get_sqrt(n, prec))
        n = int(input())


if __name__ == "__main__":
    main()