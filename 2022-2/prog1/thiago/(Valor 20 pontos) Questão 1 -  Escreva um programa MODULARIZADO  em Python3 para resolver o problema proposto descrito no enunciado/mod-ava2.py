def qtd_pessoas_equipe(a: int, b: int, c: int) -> int:
    return mdc(mdc(a, b), c)


def mdc(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a