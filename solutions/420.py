
import re

def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
    
    pattern = r'^([A-Z][a-z]?)(\d*)(([A-Z][a-z]?)(\d*))*$'
    
    if re.fullmatch(pattern, s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
