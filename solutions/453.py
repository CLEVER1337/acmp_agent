
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    target = 2 * N
    queue = [('1', 1 % target), ('2', 2 % target)]
    
    while queue:
        num_str, remainder = queue.pop(0)
        
        if remainder == 0:
            with open('OUTPUT.TXT', 'w') as f:
                f.write(num_str)
            return
        
        if len(num_str) < 10000:
            new_rem1 = (remainder * 10 + 1) % target
            queue.append((num_str + '1', new_rem1))
            
            new_rem2 = (remainder * 10 + 2) % target
            queue.append((num_str + '2', new_rem2))

if __name__ == '__main__':
    main()
