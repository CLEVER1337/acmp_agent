
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        k = int(f.readline().strip())
    
    n = len(s)
    abs_k = abs(k)
    
    if k > 0:
        result = s * abs_k
        if len(result) > 1023:
            result = result[:1023]
        print(result)
    else:
        if n % abs_k != 0:
            print("NO SOLUTION")
            return
            
        part_length = n // abs_k
        base = s[:part_length]
        
        for i in range(abs_k):
            start = i * part_length
            end = start + part_length
            if s[start:end] != base:
                print("NO SOLUTION")
                return
                
        if len(base) > 1023:
            base = base[:1023]
        print(base)

if __name__ == "__main__":
    main()
