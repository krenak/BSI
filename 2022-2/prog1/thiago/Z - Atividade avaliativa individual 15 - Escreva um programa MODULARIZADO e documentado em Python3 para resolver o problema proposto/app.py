from padroes import *
def main():
    opcao = input()
    while opcao and opcao in "abcdef":
        caract = input()
        print(eval(f"draw_{opcao}(caract)"))
        print()
        opcao = input()


if __name__ == "__main__":
    main()