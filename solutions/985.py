
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    type_sizes = {}
    index = 1
    for _ in range(n):
        parts = data[index].split()
        index += 1
        type_name = parts[0]
        size = int(parts[1])
        type_sizes[type_name] = size
    
    m = int(data[index])
    index += 1
    arrays = []
    for i in range(m):
        arrays.append(data[index])
        index += 1
    
    results = []
    for arr_desc in arrays:
        parts = arr_desc.split()
        base_type = parts[0]
        dims = []
        i = 1
        while '[' in parts[i]:
            dim_str = parts[i].strip('[];')
            dims.append(int(dim_str))
            i += 1
        
        base_size = type_sizes[base_type]
        total_size = 0
        prev_size = base_size
        
        for dim in reversed(dims):
            array_size = 16 + 4 + dim * prev_size
            prev_size = array_size
        
        total_size = 4 + prev_size
        results.append(str(total_size))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
