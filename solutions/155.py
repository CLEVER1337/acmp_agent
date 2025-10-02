
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    target = float(data[1])
    caps = list(map(float, data[2:2+n]))
    
    from itertools import permutations
    
    def compute_capacitance(sequence):
        stack = []
        for cap in sequence:
            stack.append([cap])
        
        while len(stack) > 1:
            # Try both parallel and series combinations
            new_stack = []
            for i in range(0, len(stack), 2):
                if i + 1 >= len(stack):
                    new_stack.append(stack[i])
                    continue
                
                a = stack[i]
                b = stack[i+1]
                
                # Try parallel combination
                parallel_results = []
                for val_a in a:
                    for val_b in b:
                        parallel_results.append(val_a + val_b)
                
                # Try series combination
                series_results = []
                for val_a in a:
                    for val_b in b:
                        if val_a + val_b > 0:
                            series_results.append((val_a * val_b) / (val_a + val_b))
                
                combined = parallel_results + series_results
                new_stack.append(combined)
            
            stack = new_stack
        
        return stack[0]
    
    found = False
    for r in range(1, n + 1):
        for perm in permutations(caps, r):
            results = compute_capacitance(perm)
            for result in results:
                if abs(result - target) <= 0.01:
                    found = True
                    break
            if found:
                break
        if found:
            break
    
    print("YES" if found else "NO")

if __name__ == "__main__":
    main()
