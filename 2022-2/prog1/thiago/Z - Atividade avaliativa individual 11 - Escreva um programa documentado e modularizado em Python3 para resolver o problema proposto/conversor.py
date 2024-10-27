def to_base_x(n: int, base: int) -> str:
    converted = str()
    while n:
        digit = n%base
        if digit > 9:
            digit = chr(55+digit)
        converted = str(digit) + converted
        n //= base
    return converted+"0"*(len(converted)==0)


def to_base_16(n: int) -> str:
    return to_base_x(n, 16)