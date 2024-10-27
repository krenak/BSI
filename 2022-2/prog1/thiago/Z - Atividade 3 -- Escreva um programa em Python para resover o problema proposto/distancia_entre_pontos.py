def main():
    xa = float(input())
    ya = float(input())
    xb = float(input())
    yb = float(input())
    while xa or xb or ya or yb:
        d = ((xb - xa)**2 + (yb - ya)**2)**.5
        print(f"xa={xa:.2f} ya={ya:.2f} xb={xb:.2f} yb={yb:.2f} distancia={d:.2f}")
        xa = float(input())
        ya = float(input())
        xb = float(input())
        yb = float(input())

if __name__ == "__main__":
    main()