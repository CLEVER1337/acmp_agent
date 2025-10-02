
def main():
    with open("INPUT.TXT", "r") as f:
        K = int(f.read().strip())
    
    if K <= 2:
        print(0)
        return
        
    for L in range(2, K):
        if K % (L + 1) == 0:
            result = L
            break
    else:
        result = 0
        
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
