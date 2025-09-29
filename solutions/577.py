
def main():
    with open('INPUT.TXT', 'r') as f:
        n, m = map(int, f.readline().split())
    
    count = [0] * 10
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            product = i * j
            while product > 0:
                digit = product % 10
                count[digit] += 1
                product //= 10
    
    with open('OUTPUT.TXT', 'w') as f:
        for i in range(10):
            f.write(f"{count[i]}\n")

if __name__ == "__main__":
    main()
