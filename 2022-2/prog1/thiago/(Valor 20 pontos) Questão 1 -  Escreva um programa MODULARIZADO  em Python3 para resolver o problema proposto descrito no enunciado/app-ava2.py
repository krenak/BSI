from mod import mdc, qtd_pessoas_equipe
def main():
    contrato = input()
    while contrato != "FIM":
        a, o, v = int(input()), int(input()), int(input())
        print(contrato)
        qtd_pessoas = qtd_pessoas_equipe(a, o, v)
        eq_ad = a // qtd_pessoas
        eq_op = o // qtd_pessoas
        eq_ve = v // qtd_pessoas
        print(f"{qtd_pessoas} pessoas por equipe")
        print(f"{eq_ad} equipes administrativas")
        print(f"{eq_op} equipes operacionais")
        print(f"{eq_ve} equipes de venda")
        print(f"{eq_ad+eq_op+eq_ve} equipes no total")
        contrato = input()


if __name__ == "__main__":
    main()