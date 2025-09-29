
def reverse_number(n):
    return int(str(n)[::-1])

def main():
    with open("INPUT.TXT", "r") as f:
        K = int(f.read().strip())
    
    count = 0
    for x in range(1, K):
        rev_x = reverse_number(x)
        if x + rev_x == K:
            count += 1
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
