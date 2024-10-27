def main():
    maior_area = 0
    maior_ladoa = 0
    maior_ladob = 0
    maior_ladoc = 0
    per_med_eq = 0
    qtd_eq = 0
    per_med_iso = 0
    qtd_iso = 0
    per_med_esc = 0
    qtd_esc = 0
    qtd_nao_triangulo = 0
    a = float(input())
    b = float(input())
    c = float(input())
    if a or b or c:
        while a or b or c:
            tipo = tipo_triangulo(a, b, c)
            if tipo == "NAO TRIANGULO":
                print(tipo)
                qtd_nao_triangulo += 1
            else:
                area = calc_area_triangulo(a, b, c)
                perimetro = calc_perimetro_triangulo(a, b, c)
                print(f"AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = {tipo}")
                if tipo == "EQUILATERO":
                    per_med_eq += perimetro
                    qtd_eq += 1
                elif tipo == "ISOSCELES":
                    per_med_iso += perimetro
                    qtd_iso += 1
                else:
                    per_med_esc += perimetro
                    qtd_esc += 1
                if area > maior_area:
                    maior_area = area
                    maior_ladoa = a
                    maior_ladob = b
                    maior_ladoc = c
            a = float(input())
            b = float(input())
            c = float(input())
        prct_nao_triangulo = qtd_nao_triangulo*100/(qtd_nao_triangulo+qtd_eq+qtd_iso+qtd_esc)
        if prct_nao_triangulo < 100:
            per_med_eq /= qtd_eq + (qtd_eq == 0)
            per_med_iso /= qtd_iso + (qtd_iso == 0)
            per_med_esc /= qtd_esc + (qtd_esc == 0)
            print(f"A maior area = {maior_area:.2f} eh do triangulo: lado1 = {maior_ladoa:.2f}, lado2 = {maior_ladob:.2f} e lado3 = {maior_ladoc:.2f}")
            print(f"{per_med_eq:.2f} eh o perimetro medio dos triangulos equilateros")
            print(f"{per_med_iso:.2f} eh o perimetro medio dos triangulos isoceles")
            print(f"{per_med_esc:.2f} eh o perimetro medio dos triangulos escalenos")
        print(f"Percentual de triangulos = {100-prct_nao_triangulo:.2f}")
        print(f"Percentual de nao triangulos = {prct_nao_triangulo:.2f}")
    else:
        print("NAO HA DADOS PARA PROCESSAR")


def tipo_triangulo(a: float, b: float, c: float) -> str:
    if eh_triangulo(a, b, c):
        return "NAO TRIANGULO"
    tipo = "ISOSCELES"
    if a == b and b == a:
        tipo = "EQUILATERO"
    elif a != b and b != c and a != c:
        tipo = "ESCALENO"
    return tipo


def eh_triangulo(a: float, b: float, c: float) -> bool:
    return a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b


def calc_area_triangulo(a: float, b: float, c: float) -> float:
    sp = calc_perimetro_triangulo(a, b, c)/2
    return (sp*(sp-a)*(sp-b)*(sp-c))**.5


def calc_perimetro_triangulo(a: float, b: float, c: float) -> float:
    return a + b + c


if __name__ == "__main__":
    main()