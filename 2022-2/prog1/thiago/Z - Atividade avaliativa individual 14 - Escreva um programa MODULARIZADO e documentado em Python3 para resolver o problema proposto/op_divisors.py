def qtd_divisors(n: int) -> int:
    if n <= 2:
        return n
    qtd = 2
    for c in range(2, n//2+1):
        if n % c == 0:
            qtd += 1
    return qtd