
def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    n = len(s)
    operations = []
    
    for i in range(n):
        if s[i] != t[i]:
            j = i + 1
            while j < n and s[j] != t[i]:
                j += 1
            
            operations.append((i + 1, j + 1))
            substring = s[i:j+1]
            reversed_substring = substring[::-1]
            s = s[:i] + reversed_substring + s[j+1:]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(len(operations)) + "\n")
        for op in operations:
            f.write(f"{op[0]} {op[1]}\n")

if __name__ == "__main__":
    main()
