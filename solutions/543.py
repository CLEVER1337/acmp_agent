
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        N = int(data[0])
        w = int(data[1])
        d = int(data[2])
        P = int(data[3])
    
    total_weight = 0
    for i in range(1, N):
        total_weight += i * w
    
    diff = total_weight - P
    if diff == 0:
        result = N
    else:
        result = diff // d
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
