
def main():
    with open("INPUT.TXT", "r") as f:
        K = int(f.read().strip())
    
    if K <= 2:
        print(0)
        return
        
    # Ищем минимальный делитель K-1, больший 1
    for L in range(2, K):
        if (K - 1) % L == 0:
            print(L)
            return
            
    # Если K-1 простое число больше 2
    print(K - 1)

if __name__ == "__main__":
    main()
