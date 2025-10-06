
def main():
    n = int(input().strip())
    if n <= 0:
        print("0 0")
        return
        
    min_val = (n + 5) // 6
    max_val = n * 6
    
    if n % 6 != 0:
        min_val = (n // 6) * 2 + (7 - (n % 6))
    else:
        min_val = n // 6 * 2
        
    print(f"{min_val} {max_val}")

if __name__ == "__main__":
    main()
