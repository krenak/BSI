from operacoes import *
def main():
    for c in range(1, 10002):
        eh_qp = eh_quadrado_perfeito(c)
        eh_cap = eh_capicua(c)
        if eh_qp and eh_cap:
            print(f"{c} EH QUADRADO PERFEITO E CAPICUA")
        elif eh_qp:
            print(f"{c} EH QUADRADO PERFEITO")
        elif eh_cap:
            print(f"{c} EH CAPICUA")


if __name__ == "__main__":
    main()