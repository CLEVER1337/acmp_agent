
def main():
    import sys
    n = int(sys.stdin.readline().strip())
    if n == 1:
        print("1 1")
    elif n == 2 or n == 3:
        print("No solution")
    else:
        if n % 6 == 2:
            for i in range(2, n + 1, 2):
                print(f"{i} {i}")
            print("3 1")
            print("1 3")
            for i in range(7, n + 1, 2):
                print(f"{i} {i - 2}")
            print("5 5")
        elif n % 6 == 3:
            for i in range(4, n + 1, 2):
                print(f"{i} {i}")
            print("2 2")
            print("1 3")
            print("3 1")
            for i in range(7, n + 1, 2):
                print(f"{i} {i - 2}")
            print("5 5")
        else:
            for i in range(2, n + 1, 2):
                print(f"{i} {i}")
            for i in range(1, n + 1, 2):
                print(f"{i} {i}")

if __name__ == "__main__":
    main()
