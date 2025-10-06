
def main():
    n, nAB, nBC, nAC = map(int, input().split())
    
    for kA in range(0, n + 1):
        for kB in range(0, n - kA + 1):
            for kC in range(0, n - kA - kB + 1):
                kAB = nAB - kA - kB
                kBC = nBC - kB - kC
                kAC = nAC - kA - kC
                
                if kAB >= 0 and kBC >= 0 and kAC >= 0:
                    total = kA + kB + kC + kAB + kBC + kAC
                    if total == n:
                        print("YES")
                        print(f"{kA} {kAB} {kB} {kBC} {kC} {kAC}")
                        return
                        
    print("NO")

if __name__ == "__main__":
    main()
