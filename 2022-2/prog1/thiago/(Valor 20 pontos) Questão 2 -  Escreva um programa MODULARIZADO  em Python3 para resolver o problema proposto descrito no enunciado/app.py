from mod import f_converteBaseNBase10, f_converteBaseNBase16, f_validaNumBase
def main():
    n, b = int(input()), int(input())
    while b > 1 and b < 10:
        if f_validaNumBase(n, b):
            print(f"n={n} b={b} n10={f_converteBaseNBase10(n, b)} n16={f_converteBaseNBase16(n, b)}")
        else:
            print(f"{n} INVALIDO NA BASE {b}")
        n, b = int(input()), int(input())


if __name__ == "__main__":
    main()