
def main():
    with open("INPUT.TXT", "r") as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    
    if len(s1) != len(s2):
        print(-1)
        return
        
    if s1 == s2:
        print(0)
        return
        
    doubled = s1 + s1
    pos = doubled.find(s2)
    
    if pos == -1:
        print(-1)
    else:
        print(len(s1) - pos)

if __name__ == "__main__":
    main()
