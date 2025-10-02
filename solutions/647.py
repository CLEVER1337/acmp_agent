
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    queries = list(map(int, data[2:2+m]))
    
    arr = list(range(1, n+1))
    result = []
    
    for query in queries:
        count = 0
        for i in range(n):
            count += 1
            if arr[i] == query:
                break
                
        result.append(str(count))
        
        if count > 1:
            arr.remove(query)
            arr.insert(0, query)
            
    print(' '.join(result))

if __name__ == "__main__":
    main()
