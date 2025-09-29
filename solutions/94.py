
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.readline().split()
        N = int(data[0])
        M = int(data[1])
        K = int(data[2])
    
    if N >= M:
        with open("OUTPUT.TXT", "w") as f:
            f.write("1")
        return
    
    if N <= K:
        with open("OUTPUT.TXT", "w") as f:
            f.write("NO")
        return
    
    heads = M
    hits = 0
    
    while heads > 0:
        hits += 1
        heads -= N
        if heads <= 0:
            break
        heads += K
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(hits))

if __name__ == "__main__":
    main()
