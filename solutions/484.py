
def main():
    with open('INPUT.TXT', 'r') as f:
        S = int(f.read().strip())
    
    result = []
    current = S
    
    while current >= 1:
        result.append(str(current))
        if current == 1:
            break
        
        layer = 1
        fib_prev, fib_curr = 1, 1
        total = 1
        
        while total < current:
            layer += 1
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
            total += fib_curr
        
        pos_in_layer = current - (total - fib_curr)
        
        if pos_in_layer <= fib_prev:
            current = total - fib_curr - fib_prev + pos_in_layer
        else:
            current = total - fib_curr - fib_prev + (pos_in_layer - fib_prev)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
