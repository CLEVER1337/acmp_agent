
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    names = data[1:1+n]
    
    starts = defaultdict(int)
    ends = defaultdict(int)
    components = defaultdict(int)
    
    for name in names:
        first_char = name[:3]
        last_char = name[-3:]
        starts[first_char] += 1
        ends[last_char] += 1
        
        if first_char == last_char:
            components[first_char] += 1
        else:
            components[first_char] += 1
            components[last_char] += 1
    
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for name in names:
        first_char = name[:3]
        last_char = name[-3:]
        out_degree[first_char] += 1
        in_degree[last_char] += 1
    
    deficit_nodes = []
    surplus_nodes = []
    
    all_chars = set(starts.keys()) | set(ends.keys())
    
    for char in all_chars:
        diff = out_degree[char] - in_degree[char]
        if diff > 0:
            surplus_nodes.append((char, diff))
        elif diff < 0:
            deficit_nodes.append((char, -diff))
    
    total_added = 0
    
    surplus_ptr = 0
    deficit_ptr = 0
    
    while surplus_ptr < len(surplus_nodes) and deficit_ptr < len(deficit_nodes):
        char_s, count_s = surplus_nodes[surplus_ptr]
        char_d, count_d = deficit_nodes[deficit_ptr]
        
        min_count = min(count_s, count_d)
        total_added += min_count
        
        count_s -= min_count
        count_d -= min_count
        
        if count_s == 0:
            surplus_ptr += 1
        else:
            surplus_nodes[surplus_ptr] = (char_s, count_s)
            
        if count_d == 0:
            deficit_ptr += 1
        else:
            deficit_nodes[deficit_ptr] = (char_d, count_d)
    
    for _, count in surplus_nodes[surplus_ptr:]:
        total_added += count
        
    for _, count in deficit_nodes[deficit_ptr:]:
        total_added += count
    
    if total_added == 0 and len(names) > 0:
        first_char = names[0][:3]
        last_char = names[-1][-3:]
        if first_char != last_char:
            total_added = 1
    
    print(total_added)

if __name__ == "__main__":
    main()
