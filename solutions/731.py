
import sys

def main():
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
        p = (amount * 100.0) / total
        percentages.append(p)
    
    rounded = []
    for i, (sign, amount) in enumerate(ingredients):
        p = percentages[i]
        floor_val = int(p)
        if p - floor_val < 1e-9:
            rounded_val = floor_val
        else:
            if sign == '+':
                rounded_val = int(p + 1e-9)
            else:
                rounded_val = int(p)
        rounded.append(rounded_val)
    
    current_sum = sum(rounded)
    diff = 100 - current_sum
    
    if diff != 0:
        candidates = []
        for i, (sign, amount) in enumerate(ingredients):
            p = percentages[i]
            floor_val = int(p)
            if p - floor_val < 1e-9:
                continue
            if sign == '+':
                if rounded[i] == floor_val:
                    candidates.append((p - floor_val, i, 1))
            else:
                if rounded[i] == int(p + 1e-9):
                    candidates.append((1 - (p - floor_val), i, -1))
        
        candidates.sort(key=lambda x: (-x[0], x[2]))
        
        for _, idx, direction in candidates:
            if diff > 0 and direction == 1:
                rounded[idx] += 1
                diff -= 1
            elif diff < 0 and direction == -1:
                rounded[idx] -= 1
                diff += 1
            if diff == 0:
                break
    
    for val in rounded:
        print(val)

if __name__ == "__main__":
    main()
