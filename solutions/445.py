
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
        name = parts[0].lower()
        quantity = float(parts[1])
        plan.append((name, quantity))
    
    old_prices = {}
    start_old = 1 + n + 1
    for i in range(start_old, start_old + k1):
        parts = data[i].split()
        name = parts[0].lower()
        price = float(parts[1])
        old_prices[name] = price
    
    new_prices = {}
    start_new = start_old + k1 + 1
    for i in range(start_new, start_new + k2):
        parts = data[i].split()
        name = parts[0].lower()
        price = float(parts[1])
        new_prices[name] = price
    
    total_planned_cost = 0.0
    for name, quantity in plan:
        total_planned_cost += quantity * old_prices[name]
    
    max_new_cost = total_planned_cost - d
    
    benefits = []
    for name, quantity in plan:
        old_price = old_prices[name]
        new_price = new_prices.get(name, float('inf'))
        benefit_per_unit = old_price - new_price
        benefits.append((benefit_per_unit, quantity, name))
    
    benefits.sort(reverse=True, key=lambda x: x[0])
    
    result = [0.0] * n
    remaining_cost = max_new_cost
    
    for i, (benefit_per_unit, quantity, name) in enumerate(benefits):
        old_price = old_prices[name]
        new_price = new_prices[name]
        
        max_possible_cost = quantity * old_price
        
        if benefit_per_unit <= 0:
            result[i] = 0.0
            continue
            
        if remaining_cost <= 0:
            result[i] = 0.0
            continue
            
        max_affordable_quantity = remaining_cost / old_price
        
        if max_affordable_quantity >= quantity:
            result[i] = quantity
            remaining_cost -= quantity * old_price
        else:
            result[i] = max_affordable_quantity
            remaining_cost = 0.0
    
    output_lines = []
    for name, quantity in plan:
        for i, (benefit_per_unit, q, n_name) in enumerate(benefits):
            if n_name == name:
                output_lines.append(str(result[i]))
                break
    
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
