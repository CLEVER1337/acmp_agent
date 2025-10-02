
def main():
    with open('INPUT.TXT', 'r') as f:
        N, M = map(int, f.readline().split())
    
    count = [0] * 10
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            product = i * j
            while product > 0:
                digit = product % 10
                count[digit] += 1
                product //= 10
    
    with open('OUTPUT.TXT', 'w') as f:
        for cnt in count:
            f.write(f"{cnt}\n")

if __name__ == "__main__":
    main()
