def is_between_y1_y2(x: float, y: float) -> bool:
    return y < get_y1(x) and y > get_y2(x) if y >= 0 else y > get_y1(x) and y < get_y2(x)


def get_y1(x: float) -> float:
    return x*3


def get_y2(x: float) -> float:
    return x/3