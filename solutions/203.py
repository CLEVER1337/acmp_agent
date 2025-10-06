
def main():
    s1 = input().strip()
    s2 = input().strip()
    
    if len(s1) != len(s2):
        print(-1)
        return
        
    if s1 == s2:
        print(0)
        return
        
    n = len(s1)
    doubled = s1 + s1
    
    for shift in range(1, n):
        if doubled[n - shift:2 * n - shift] == s2:
            print(shift)
            return
            
    print(-1)

if __name__ == "__main__":
    main()
