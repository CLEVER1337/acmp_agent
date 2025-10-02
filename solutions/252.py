
def convert_to_grams(value, unit):
    multipliers = {
        'm': 1e-3,
        'k': 1e3,
        'M': 1e6,
        'G': 1e9,
        '': 1
    }
    
    if len(unit) > 1:
        prefix = unit[0]
        base_unit = unit[1]
    else:
        prefix = ''
        base_unit = unit[0]
    
    multiplier = multipliers[prefix]
    
    if base_unit == 'g':
        return value * multiplier
    elif base_unit == 'p':
        return value * multiplier * 16380
    elif base_unit == 't':
        return value * multiplier * 1e6

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        pipelines = []
        for i in range(n):
            line = f.readline().strip()
            parts = line.split()
            value = int(parts[0])
            unit = parts[1]
            pipelines.append((value, unit, i, line))
    
    pipelines_with_grams = []
    for value, unit, idx, original in pipelines:
        grams = convert_to_grams(value, unit)
        pipelines_with_grams.append((grams, idx, original))
    
    pipelines_with_grams.sort(key=lambda x: (x[0], x[1]))
    
    with open('OUTPUT.TXT', 'w') as f:
        for pipeline in pipelines_with_grams:
            f.write(pipeline[2] + '\n')

if __name__ == '__main__':
    main()
