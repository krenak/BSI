#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#20222bsi0075_at7.py
#
#Copyright 2022, Thiago Borges Pereira
#

def main():
    maior_aus = -1
    turma_maior_aus = ""
    menor_aus = 101
    turma_menor_aus = ""
    turmas_ausentes = 0
    qtd_turmas = int(input())
    for i in range(qtd_turmas):
        ident = input()
        qtd_alunos = int(input())
        qtd_ausentes = 0
        for al in range(qtd_alunos):
            matricula = input()
            estado = input().upper()
            qtd_ausentes += estado == "A"
        ausencia = qtd_ausentes * 100 / qtd_alunos
        if ausencia > 20:
            turmas_ausentes += 1
        if ausencia > maior_aus:
            maior_aus = ausencia
            turma_maior_aus = ident
        if ausencia < menor_aus:
            menor_aus = ausencia
            turma_menor_aus = ident
        print(f"TURMA={ident} AUSENCIA={ausencia:.2f}%")
    print(f"TURMA COM MAIOR PORCENTAGEM DE AUSENCIA={turma_maior_aus} AUSENCIA={maior_aus:.2f}%")
    print(f"TURMA COM MENOR PORCENTAGEM DE AUSENCIA={turma_menor_aus} AUSENCIA={menor_aus:.2f}%")
    print(f"{turmas_ausentes} TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%")
if __name__ == "__main__":
    main()