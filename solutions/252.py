
def to_grams(s):
    num, unit = s.split()
    num = int(num)
    
    prefix_multiplier = 1
    if unit[0] in ['m', 'k', 'M', 'G']:
        prefix = unit[0]
        unit_char = unit[1]
        if prefix == 'm':
            prefix_multiplier = 1e-3
        elif prefix == 'k':
            prefix_multiplier = 1e3
        elif prefix == 'M':
            prefix_multiplier = 1e6
        elif prefix == 'G':
            prefix_multiplier = 1e9
    else:
        unit_char = unit[0]
    
    if unit_char == 'g':
        base_multiplier = 1
    elif unit_char == 'p':
        base_multiplier = 16380
    elif unit_char == 't':
        base_multiplier = 1e6
    
    return num * prefix_multiplier * base_multiplier

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        pipelines = []
        for i in range(n):
            line = f.readline().strip()
            pipelines.append((line, to_grams(line), i))
    
    pipelines.sort(key=lambda x: (x[1], x[2]))
    
    with open('OUTPUT.TXT', 'w') as f:
        for pipeline in pipelines:
            f.write(pipeline[0] + '\n')

if __name__ == '__main__':
    main()
