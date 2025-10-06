
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
    for i in range(1, n + 1):
        parts = data[i].split()
        name = parts[0].lower()
        quantity = float(parts[1])
        plan.append((name, quantity))
    
    old_prices = {}
    start_old = n + 1
    for i in range(start_old, start_old + k1):
        parts = data[i].split()
        name = parts[0].lower()
        price = float(parts[1])
        old_prices[name] = price
    
    new_prices = {}
    start_new = start_old + k1
    for i in range(start_new, start_new + k2):
        parts = data[i].split()
        name = parts[0].lower()
        price = float(parts[1])
        new_prices[name] = price
    
    items = []
    total_planned_cost = 0.0
    for name, quantity in plan:
        old_price = old_prices[name]
        new_price = new_prices.get(name, float('inf'))
        planned_cost = quantity * old_price
        total_planned_cost += planned_cost
        saving_per_unit = old_price - new_price
        items.append((saving_per_unit, planned_cost, quantity, name))
    
    items.sort(key=lambda x: x[0], reverse=True)
    
    result = [0.0] * n
    remaining_d = d
    
    for i, (saving_per_unit, planned_cost, quantity, name) in enumerate(items):
        if saving_per_unit <= 0:
            continue
        
        if remaining_d >= planned_cost:
            result[i] = quantity
            remaining_d -= planned_cost
        else:
            result[i] = remaining_d / old_prices[name]
            remaining_d = 0
    
    output_lines = []
    for i in range(n):
        original_index = -1
        for idx, (name, _) in enumerate(plan):
            if name == items[i][3]:
                original_index = idx
                break
        output_lines.append((original_index, f"{result[i]:.6f}"))
    
    output_lines.sort(key=lambda x: x[0])
    for idx, line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
