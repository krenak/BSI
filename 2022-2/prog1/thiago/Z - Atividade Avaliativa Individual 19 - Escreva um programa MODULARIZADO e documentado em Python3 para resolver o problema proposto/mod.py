from functools import lru_cache
def calc_integral(n: int) -> float:
    x = 0
    h = 1/n
    area = 0
    for _ in range(n):
        area += (calc_y(x) + calc_y(x+h))*h/2
        x += h
    return 4*area


@lru_cache(maxsize=None)
def calc_y(x: float) -> float:
    return 1/(1+x**2)