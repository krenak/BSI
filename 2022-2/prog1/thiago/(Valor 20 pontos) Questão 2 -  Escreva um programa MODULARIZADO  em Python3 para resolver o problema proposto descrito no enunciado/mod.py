def f_validaNumBase(n: int, b: int) -> bool:
    while n:
        if n%10 >= b:
            return False
        n //= 10
    return True


def f_converteBaseNBase10(n: int, b: int) -> int:
    conv = 0
    fator = 0
    while n:
        conv += n%10*b**fator
        n //= 10
        fator += 1
    return conv



def f_converteBaseNBase16(n: int, b: int) -> str:
    n = f_converteBaseNBase10(n, b)
    conv = ""
    while n:
        el = n % 16
        conv += chr(55+el) if el >= 10 else str(el)
        n //= 16
    return conv[::-1] + ("" if conv else "0")