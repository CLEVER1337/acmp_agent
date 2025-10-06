
import sys

def main():
    data = sys.stdin.read().splitlines()
    index = 0
    n = int(data[index])
    index += 1
    type_sizes = {}
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
        name_part = parts[1]
        dims = []
        i = 0
        while i < len(name_part):
            if name_part[i] == '[':
                j = i + 1
                num_str = ''
                while j < len(name_part) and name_part[j] != ']':
                    num_str += name_part[j]
                    j += 1
                dims.append(int(num_str))
                i = j
            i += 1
            
        base_size = type_sizes[base_type]
        total_size = 0
        for dim in reversed(dims):
            if total_size == 0:
                total_size = base_size * dim
            else:
                total_size = dim * (20 + total_size)
            total_size += 20
            
        results.append(str(total_size + 4))
        
    print('\n'.join(results))

if __name__ == "__main__":
    main()
