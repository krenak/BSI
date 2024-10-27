from mdc import calc_mdc

def main():
    for _ in range(25):
        a = int(input())
        b = int(input())
        c = int(input())
        mdc = calc_mdc(calc_mdc(a, b), c)
        print(f"MDC({a}, {b}, {c})={mdc}")


if __name__ == "__main__":
    main()