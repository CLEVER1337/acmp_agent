
def main():
    with open("INPUT.TXT", "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()
    
    n = len(s)
    m = len(t)
    
    if m == 0:
        print("YES")
        return
        
    # Проверяем, является ли t подстрокой бесконечной строки s, повторенной много раз
    for start_pos in range(n):
        # Пробуем начать с каждой позиции в s
        i = start_pos
        j = 0
        valid = True
        
        while j < m:
            if t[j] != s[i % n]:
                valid = False
                break
            j += 1
            i += 1
        
        if valid:
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    main()
