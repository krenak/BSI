from math import floor
def eh_quadrado_perfeito(n: int):
    return n == floor(n**.5)**2


def eh_capicua(n: int) -> bool:
    return n == inverte_num(n)


def inverte_num(n: int) -> int:
    inverso = 0
    while n:
        inverso = inverso*10 + n%10
        n //= 10
    return inverso