
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
    for _ in range(m):
        arrays.append(data[index])
        index += 1
    
    results = []
    for arr_desc in arrays:
        parts = arr_desc.split()
        base_type = parts[0]
        name_part = parts[1]
        
        dimensions = []
        current = name_part
        while '[' in current:
            start = current.find('[')
            end = current.find(']')
            dim = int(current[start+1:end])
            dimensions.append(dim)
            current = current[:start]
        
        base_size = type_sizes[base_type]
        total_size = 0
        
        for i in range(len(dimensions)):
            dims = dimensions[i:]
            size_for_level = base_size
            for dim in dims[1:]:
                size_for_level = 4 + 16 + 4 + dim * size_for_level
            total_size = 4 + 16 + 4 + dims[0] * size_for_level
        
        results.append(str(total_size))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
