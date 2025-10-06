
def main():
    s1 = input().strip()
    s2 = input().strip()
    
    if len(s1) != len(s2):
        print("No")
        return
        
    n = len(s1)
    if n == 0:
        print("Yes")
        print(0)
        return
        
    doubled = s1 + s1
    found_index = doubled.find(s2)
    
    if found_index == -1:
        print("No")
    else:
        k = n - found_index
        print("Yes")
        print(k)

if __name__ == "__main__":
    main()
