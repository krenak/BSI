def main():
    a = int(input())
    b = int(input())
    c = int(input())
    while a or b or c:
        print(f"MAIOR( {a} , {b} , {c} ) = ", end="")
        if a >= b and a >= c:
            print(a)
        elif b >= a and b >= c:
            print(b)
        else:
            print(c)
        a = int(input())
        b = int(input())
        c = int(input())

if __name__ == "__main__":
    main()
    