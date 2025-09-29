
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = list(map(int, data[1:1+n]))
    
    total_capacity = sum(k)
    max_capacity = max(k)
    rest_capacity = total_capacity - max_capacity
    
    if max_capacity <= rest_capacity:
        result = total_capacity // 2
    else:
        result = rest_capacity
    
    print(result)

if __name__ == "__main__":
    main()
