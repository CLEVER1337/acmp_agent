
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
        k = int(f.readline().strip())
    
    if k > 0:
        result = s * k
        if len(result) > 1023:
            result = result[:1023]
        print(result)
    else:
        n = abs(k)
        if len(s) % n != 0:
            print("NO SOLUTION")
            return
        
        part_length = len(s) // n
        base = s[:part_length]
        
        for i in range(n):
            start = i * part_length
            end = start + part_length
            if s[start:end] != base:
                print("NO SOLUTION")
                return
        
        if len(base) > 1023:
            base = base[:1023]
        print(base)

if __name__ == '__main__':
    main()
