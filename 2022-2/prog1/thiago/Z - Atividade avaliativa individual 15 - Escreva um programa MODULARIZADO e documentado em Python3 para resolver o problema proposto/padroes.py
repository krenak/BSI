def draw_a(ch: str) -> str:
    txt = ""
    for _ in range(6):
        txt += ch*6 + "\n"
    return txt


def draw_b(ch: str) -> str:
    txt = ""
    for i in range(1, 7):
        txt += (ch*i).ljust(6) + "\n"
    return txt


def draw_c(ch: str) -> str:
    txt = ""
    for i in range(1, 7):
        txt += (ch*i).rjust(6) + "\n"
    return txt


def draw_d(ch: str) -> str:
    txt = ""
    for i in range(1, 8, 2):
        txt += (ch*i).center(7) + "\n"
    for i in range(5, 0, -2):
        txt += (ch*i).center(7) + "\n"
    return txt


def draw_e(ch: str) -> str:
    txt = ""
    for i in range(6, 0, -1):
        txt += (ch*i).ljust(6) + "\n"
    return txt


def draw_f(ch: str) -> str:
    txt = ""
    for i in range(6, 0, -1):
        txt += (ch*i).rjust(6) + "\n"
    return txt