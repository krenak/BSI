from conversor import to_base_16
def main():
    n = int(input())
    while n >= 0:
        print(f"BASE10={n} BASE16={to_base_16(n)}")
        n = int(input())


if __name__ == "__main__":
    main()