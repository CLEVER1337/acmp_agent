
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    a_list = list(map(int, data[1:1+n]))
    b_list = list(map(int, data[1+n:1+2*n]))
    
    indices = list(range(n))
    indices.sort(key=lambda i: (b_list[i], a_list[i]))
    
    total_time = 0
    for i in indices:
        total_time += a_list[i]
        if total_time > b_list[i]:
            print(-1)
            return
            
    print(" ".join(str(i+1) for i in indices))

if __name__ == "__main__":
    main()
