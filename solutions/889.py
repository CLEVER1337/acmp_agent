
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    k = int(data[0])
    m = int(data[1])
    connections = []
    index = 2
    for i in range(m):
        p = int(data[index])
        h = int(data[index + 1])
        index += 2
        connections.append((p, h))
    
    left = {}
    right = {}
    for p, h in connections:
        if p not in left:
            left[p] = h
        else:
            if h > left[p]:
                left[p] = h
                
        if p - 1 not in right:
            right[p - 1] = h
        else:
            if h > right[p - 1]:
                right[p - 1] = h
    
    current_thread = k
    current_height = float('inf')
    
    while True:
        found = False
        
        if current_thread in left and left[current_thread] < current_height:
            current_height = left[current_thread]
            current_thread += 1
            found = True
        elif current_thread - 1 in right and right[current_thread - 1] < current_height:
            current_height = right[current_thread - 1]
            current_thread -= 1
            found = True
            
        if not found:
            break
            
    print(current_thread)

if __name__ == "__main__":
    main()
