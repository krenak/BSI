from mod import is_between_y1_y2
def main():
    x, y = float(input()), float(input())
    while x or y:
        print("INTERIOR" if is_between_y1_y2(x, y) else "EXTERIOR")
        x, y = float(input()), float(input())


if __name__ == "__main__":
    main()