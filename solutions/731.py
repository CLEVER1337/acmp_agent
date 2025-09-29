
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    ingredients = []
    total = 0
    for i in range(1, n + 1):
        parts = data[i].split()
        sign = parts[0]
        amount = int(parts[1])
        total += amount
        ingredients.append((sign, amount))
    
    percentages = []
    for sign, amount in ingredients:
        p = (amount * 100) / total
        percentages.append(p)
    
    floor_sum = 0
    remainders = []
    results = []
    
    for i, p in enumerate(percentages):
        floor_val = int(p)
        remainder = p - floor_val
        floor_sum += floor_val
        remainders.append((i, remainder, ingredients[i][0]))
        results.append(floor_val)
    
    remaining = 100 - floor_sum
    remainders.sort(key=lambda x: (-x[1], x[2] == '+'))
    
    for i in range(remaining):
        idx, _, sign = remainders[i]
        results[idx] += 1
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
