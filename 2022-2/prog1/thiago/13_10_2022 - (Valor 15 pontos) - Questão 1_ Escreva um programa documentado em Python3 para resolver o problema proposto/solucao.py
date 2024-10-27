def main():
    qtd_eq = 0
    qtd_esc = 0
    qtd_iso = 0
    qtd_naotri = 0
    media_eq = 0
    media_esc = 0
    media_iso = 0
    maior_area = 0
    maior_lado1 = 0
    maior_lado2 = 0
    maior_lado3 = 0
    
    a = float(input())
    b = float(input())
    c = float(input())
    if a or b or c:
        while a or b or c:
            if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
                print("NAO TRIANGULO")
                qtd_naotri += 1
            else:
                sp = (a + b + c)/2
                area = (sp*(sp-a)*(sp-b)*(sp-c))**.5
                print(f"AREA = {area:.2f} PERIMETRO = {sp*2:.2f} TIPO =", end=" ")
                if a == b and b == c:
                    print("EQUILATERO")
                    qtd_eq += 1
                    media_eq += a + b + c
                elif a == b or b == c or a == c:
                    print("ISOSCELES")
                    qtd_iso += 1
                    media_iso += a + b + c
                else:
                    print("ESCALENO")
                    media_esc += a + b + c
                    qtd_esc += 1
                if area > maior_area:
                    maior_area = area
                    maior_lado1 = a
                    maior_lado2 = b
                    maior_lado3 = c
            a = float(input())
            b = float(input())
            c = float(input())
        percentual_tri = 100*(qtd_eq+qtd_esc+qtd_iso)/(qtd_eq+qtd_esc+qtd_iso+qtd_naotri)
        if qtd_eq or qtd_esc or qtd_iso:
            media_eq /= qtd_eq + (qtd_eq == 0)
            media_esc /= qtd_esc + (qtd_esc == 0)
            media_iso /= qtd_iso + (qtd_iso == 0)
            print(f"A maior area = {maior_area:.2f} eh do triangulo: lado1 = {maior_lado1:.2f}, lado2 = {maior_lado2:.2f} e lado3 = {maior_lado3:.2f}")
            print(f"{media_eq:.2f} eh o perimetro medio dos triangulos equilateros")
            print(f"{media_iso:.2f} eh o perimetro medio dos triangulos isoceles")
            print(f"{media_esc:.2f} eh o perimetro medio dos triangulos escalenos")
        print(f"Percentual de triangulos = {percentual_tri:.2f}")
        print(f"Percentual de nao triangulos = {100-percentual_tri:.2f}")
    else:
        print("NAO HA DADOS PARA PROCESSAR")


if __name__ == "__main__":
    main()