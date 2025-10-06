
def main():
    n = int(input().strip())
    if n == 1:
        print("1 1")
    elif n == 2 or n == 3:
        print("No solution")
    else:
        if n % 6 == 2:
            evens = list(range(2, n + 1, 2))
            odds = list(range(1, n + 1, 2))
            evens[0], evens[1] = evens[1], evens[0]
            evens.pop()
            evens.append(4)
            result = evens + odds
        elif n % 6 == 3:
            evens = list(range(4, n + 1, 2))
            odds = list(range(1, n + 1, 2))
            evens.append(2)
            odds.remove(1)
            odds.remove(3)
            odds.append(1)
            odds.append(3)
            result = evens + odds
        else:
            evens = list(range(2, n + 1, 2))
            odds = list(range(1, n + 1, 2))
            result = evens + odds
        
        for i in range(n):
            print(f"{i + 1} {result[i]}")

if __name__ == "__main__":
    main()
