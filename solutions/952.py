
def main():
    n, m = map(int, input().split())
    
    if n == 0 and m > 0:
        print("Impossible")
        return
        
    min_cost = max(n, m)
    max_cost = n + max(0, m - 1)
    
    if n == 0:
        min_cost = 0
        max_cost = 0
        
    print(f"{min_cost} {max_cost}")

if __name__ == "__main__":
    main()
