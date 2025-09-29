
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    m, n = map(int, data[0].split())
    k = int(data[1])
    
    sets = [set() for _ in range(n)]
    element_sets = [set() for _ in range(m + 1)]
    
    output_lines = []
    
    for i in range(2, 2 + k):
        parts = data[i].split()
        op = parts[0]
        
        if op == "ADD":
            element = int(parts[1])
            set_num = int(parts[2])
            sets[set_num - 1].add(element)
            element_sets[element].add(set_num)
            
        elif op == "LISTSET":
            set_num = int(parts[1])
            elements = sorted(sets[set_num - 1])
            if elements:
                output_lines.append(" ".join(map(str, elements)))
            else:
                output_lines.append("-1")
                
        elif op == "LISTSETSOF":
            element = int(parts[1])
            set_nums = sorted(element_sets[element])
            if set_nums:
                output_lines.append(" ".join(map(str, set_nums)))
            else:
                output_lines.append("-1")
    
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()
