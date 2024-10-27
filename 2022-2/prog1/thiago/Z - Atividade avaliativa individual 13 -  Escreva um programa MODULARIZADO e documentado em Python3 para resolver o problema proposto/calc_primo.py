def eh_primo(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for c in range(3, int(n**.5)+1, 2):
        if n % c == 0:
            return False
    return n > 1