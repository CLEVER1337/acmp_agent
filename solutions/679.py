
def main():
    n = int(input().strip())
    
    if n == 2:
        print("2 1")
        return
        
    if n == 3:
        print("3 1")
        return
        
    if n == 4:
        print("2 2")
        return
        
    if n % 3 == 0:
        count = n // 3
        print(f"3 {count}")
        return
        
    if n % 3 == 1:
        count_3 = (n - 4) // 3
        count_2 = 2
        if count_3 > 0:
            print(f"2 {count_2}")
            print(f"3 {count_3}")
        else:
            print(f"2 {count_2}")
        return
        
    if n % 3 == 2:
        count_3 = (n - 2) // 3
        print(f"2 1")
        if count_3 > 0:
            print(f"3 {count_3}")
        return

if __name__ == "__main__":
    main()
