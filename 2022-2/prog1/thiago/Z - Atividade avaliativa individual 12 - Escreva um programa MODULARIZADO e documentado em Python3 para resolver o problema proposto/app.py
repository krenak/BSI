from calc_triangulo import area_triangulo
def main():
    a, b = float(input()), float(input())
    while a or b:
        print(f"AREA={area_triangulo(a, b):.5f} A={a:.5f} B={b:.5f}")
        a, b = float(input()), float(input())


if __name__ == "__main__":
    main()