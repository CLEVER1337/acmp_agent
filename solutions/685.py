
def main():
    A1, A2, A3, B1, B2, B3 = map(int, input().split())
    prices = [A1, A2, A3]
    capacities = [B1, B2, B3]
    prices.sort(reverse=True)
    capacities.sort(reverse=True)
    total = sum(prices[i] * capacities[i] for i in range(3))
    print(total)

if __name__ == "__main__":
    main()
