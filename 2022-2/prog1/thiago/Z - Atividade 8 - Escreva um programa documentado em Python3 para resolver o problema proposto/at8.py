#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#20222bsi0075_at8.py
#
#Copyright 2022, Thiago Borges Pereira
#

def main():
    total = 0
    vencedor = 9999
    total_vencedor = 0
    f_um = float(input())
    f_dois = float(input())
    f_tres = float(input())
    equipe = int(input())
    while equipe != 9999:
        d_um = float(input())
        d_dois = float(input())
        d_tres = float(input())
        d_um = ((d_um - f_um)**2)**.5 # (x**2)**.5 = |x|
        d_dois = ((d_dois - f_dois)**2)**.5
        d_tres = ((d_tres - f_tres)**2)**.5
        p_um = 100 - 20*(d_um >= 3) - (d_um - 5)/5*(d_um > 5)
        p_dois = 100 - 20*(d_dois >= 3) - (d_dois - 5)/5*(d_dois > 5)
        p_tres = 100 - 20*(d_tres >= 3) - (d_tres - 5)/5*(d_tres > 5)
        total = p_um + p_dois + p_tres

        print(f"EQUIPE={equipe} P1={p_um:.2f} P2={p_dois:.2f} P3={p_tres:.2f} PT={total:.2f}")
        if total > total_vencedor:
            total_vencedor = total
            vencedor = equipe
        total = 0
        equipe = int(input())
    if vencedor != 9999:
        print(f"EQUIPE VENCEDORA={vencedor} PONTUACAO TOTAL={total_vencedor:.2f}")
    else:
        print("SEM EQUIPES CADASTRADAS")
if __name__ == "__main__":
    main()