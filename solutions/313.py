
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    routes = list(map(int, data[1:1+n]))
    
    last_occurrence = {}
    max_wait = 0
    
    for i, route in enumerate(routes):
        if route in last_occurrence:
            distance = i - last_occurrence[route] - 1
            if distance > max_wait:
                max_wait = distance
        last_occurrence[route] = i
        
    print(max_wait)

if __name__ == "__main__":
    main()
