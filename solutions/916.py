
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    k = int(data[1])
    costs = list(map(int, data[2:2+n]))
    
    costs.sort(reverse=True)
    
    total_cost = 0
    multiplier = 1
    
    for i in range(n):
        if i % k == 0 and i != 0:
            multiplier += 1
        total_cost += multiplier * costs[i]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_cost))

if __name__ == '__main__':
    main()
