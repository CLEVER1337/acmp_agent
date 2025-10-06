
def convert_to_grams(s):
    num, unit = s.split()
    num = int(num)
    prefix_multiplier = 1
    if unit[0] in ['m', 'k', 'M', 'G']:
        prefix = unit[0]
        base_unit = unit[1]
        if prefix == 'm':
            prefix_multiplier = 1e-3
        elif prefix == 'k':
            prefix_multiplier = 1e3
        elif prefix == 'M':
            prefix_multiplier = 1e6
        elif prefix == 'G':
            prefix_multiplier = 1e9
    else:
        base_unit = unit[0]
    
    if base_unit == 'g':
        grams = num * prefix_multiplier
    elif base_unit == 'p':
        grams = num * prefix_multiplier * 16380
    elif base_unit == 't':
        grams = num * prefix_multiplier * 1e6
    
    return grams

def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    pipes = []
    for i in range(1, n + 1):
        pipes.append(data[i].strip())
    
    converted = []
    for i, pipe in enumerate(pipes):
        grams = convert_to_grams(pipe)
        converted.append((grams, i, pipe))
    
    converted.sort(key=lambda x: (x[0], x[1]))
    
    for item in converted:
        print(item[2])

if __name__ == "__main__":
    main()
