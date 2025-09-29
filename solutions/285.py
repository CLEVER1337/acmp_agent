
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    total_burn_time = sum(a)
    max_possible_time = total_burn_time + (n - 1)
    
    if m > max_possible_time:
        print("no")
        return
        
    min_possible_time = 0
    current_time = 0
    
    for burn_time in sorted(a):
        if current_time >= burn_time:
            min_possible_time = current_time + burn_time
            current_time += 1
        else:
            min_possible_time += burn_time
            current_time = burn_time
            
    if m >= min_possible_time:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
