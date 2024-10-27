def main():
    mais_votado = ""
    estado_mais_votado = ""
    perc_mais_votado = 0
    estado = input()
    while estado != "FIM":
        id1 = int(input())
        cand1 = input()
        id2 = int(input())
        cand2 = input()
        total_eleitores = total_cand1 = total_cand2 = total_branco = total_nulo = 0
        id_urna = int(input())
        while id_urna:
            qtd_eleitores = int(input())
            qtd_cand1 = int(input())
            qtd_cand2 = int(input())
            qtd_branco = int(input())
            qtd_nulo = int(input())
            total_eleitores += qtd_eleitores
            total_cand1 += qtd_cand1
            total_cand2 += qtd_cand2
            total_branco += qtd_branco
            total_nulo += qtd_nulo
            id_urna = int(input())
        if total_cand1 + total_cand2:
            perc_cand1 = total_cand1/(total_cand1 + total_cand2)*100
            perc_cand2 = total_cand2/(total_cand1 + total_cand2)*100
        else:
            perc_cand1 = perc_cand2 = 0
        print(estado)
        print(f"{total_eleitores} eleitores")
        print(f"{cand1} obteve {total_cand1} votos, totalizando {perc_cand1:.2f}% dos votos validos")
        print(f"{cand2} obteve {total_cand2} votos, totalizando {perc_cand2:.2f}% dos votos validos")
        print(f"{total_cand1 + total_cand2} votos validos")
        print(f"{total_nulo} votos nulos")
        print(f"{total_branco} votos em branco")
        print(f"{total_eleitores - total_cand1 - total_cand2 - total_branco - total_nulo} abstencoes")
        if total_cand1 >= total_cand2:
            vencedor = cand1
            perc_votos = perc_cand1
        else:
            vencedor = cand2
            perc_votos = perc_cand2
        print(f"Vencedor(a): {vencedor}\n")
        if perc_votos > perc_mais_votado:
            mais_votado = vencedor
            estado_mais_votado = estado
            perc_mais_votado = perc_votos
        estado = input()
    if perc_mais_votado:
        print(f"A(o) candidata(o) mais votada(o) no pais eh {mais_votado} do estado de ESPIRITO SANTO com {perc_mais_votado:.2f}% dos votos.")


if __name__ == "__main__":
    main()