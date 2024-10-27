def main():
    num = int(input())
    div = int(input())
    if num <= 0 or div <= 0:
        print("ENTRADA INVALIDA")
    else:
        quoc = 0
        while num >= div:
            num -= div
            quoc += 1
        print(f"QUOCIENTE={quoc}")
if __name__ == "__main__":
    main()