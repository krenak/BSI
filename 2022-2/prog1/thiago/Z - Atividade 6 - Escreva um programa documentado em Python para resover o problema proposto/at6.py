#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#20222bsi0075_at6.py
#
#Copyright 2022, Thiago Borges Pereira
#

def main():
    segundos = 0
    massa = float(input())
    while massa >= 0:
        print(f"MASSA INICIAL={massa:.3f}", end=" ")
        while massa >= 0.5:
            massa /= 2
            segundos += 50
        horas, segundos = segundos // 3600, segundos % 3600
        minutos, segundos = segundos // 60, segundos % 60
        print(f"MASSA FINAL={massa:.3f} TEMPO DECORRIDO={horas}:{minutos}:{segundos}")

        segundos = 0
        massa = float(input())
    print("FIM")


if __name__ == "__main__":
    main()