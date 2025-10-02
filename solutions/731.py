
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    ingredients = []
    total = 0
    for i in range(1, n+1):
        parts = data[i].split()
        sign = parts[0]
        amount = int(parts[1])
        total += amount
        ingredients.append((sign, amount))
    
    percentages = []
    for sign, amount in ingredients:
        p = (amount / total) * 100
        percentages.append(p)
    
    rounded = [int(p) for p in percentages]
    remainder = 100 - sum(rounded)
    
    diffs = []
    for i, (sign, p) in enumerate(zip([ing[0] for ing in ingredients], percentages)):
        diff = p - rounded[i]
        if sign == '+':
            priority = diff
        else:
            priority = -diff
        diffs.append((priority, i))
    
    diffs.sort(reverse=True, key=lambda x: x[0])
    
    for i in range(remainder):
        idx = diffs[i][1]
        rounded[idx] += 1
    
    for r in rounded:
        print(r)

if __name__ == "__main__":
    main()
