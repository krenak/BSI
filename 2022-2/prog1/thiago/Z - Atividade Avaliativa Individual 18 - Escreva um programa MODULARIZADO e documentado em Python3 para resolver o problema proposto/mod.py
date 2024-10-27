def get_sqrt(n: float, aprox: int) -> float:
    x = n/2
    for c in range(aprox-1):
        x = (x**2 + n)/(2*x)
    return x