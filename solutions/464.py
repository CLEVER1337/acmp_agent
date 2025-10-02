
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
    
    if n == 1:
        result = 0
    else:
        length = 1
        k = 0
        
        while length * 2 < n:
            length *= 2
            k += 1
        
        pos_in_block = n - length - 1
        result = (k % 3 + pos_in_block) % 3
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
