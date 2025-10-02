
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].split()
    n = int(first_line[0])
    d = float(first_line[1])
    k1 = int(first_line[2])
    k2 = int(first_line[3])
    
    plan = []
    for i in range(1, 1 + n):
        parts = data[i].split()
        name = ' '.join(parts[:-1]).lower()
        quantity = float(parts[-1])
        plan.append((name, quantity))
    
    old_prices = {}
    new_prices = {}
    
    current_line = n + 1
    
    for i in range(current_line, current_line + k1):
        parts = data[i].split()
        if not parts:
            continue
        name = ' '.join(parts[:-1]).lower()
        price = float(parts[-1])
        old_prices[name] = price
    
    current_line += k1 + 1
    
    for i in range(current_line, current_line + k2):
        parts = data[i].split()
        if not parts:
            continue
        name = ' '.join(parts[:-1]).lower()
        price = float(parts[-1])
        new_prices[name] = price
    
    savings = []
    for name, quantity in plan:
        old_price = old_prices[name]
        new_price = new_prices.get(name, float('inf'))
        saving_per_unit = old_price - new_price
        savings.append((saving_per_unit, quantity, name))
    
    savings.sort(reverse=True)
    
    result = [0.0] * n
    remaining_d = d
    
    for i, (saving_per_unit, quantity, name) in enumerate(savings):
        if saving_per_unit <= 0:
            continue
        
        max_possible = min(quantity, remaining_d / old_prices[name])
        if max_possible * saving_per_unit >= quantity * saving_per_unit:
            result[i] = quantity
            remaining_d -= quantity * old_prices[name]
        else:
            result[i] = max_possible
            remaining_d -= max_possible * old_prices[name]
            break
    
    output_lines = []
    for name, _ in plan:
        for idx, (_, _, item_name) in enumerate(savings):
            if item_name == name:
                output_lines.append(str(result[idx]))
                break
    
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
