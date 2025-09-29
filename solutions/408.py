
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().splitlines()
    
    if not data:
        print("Impossible.")
        return
        
    try:
        k, n = map(int, data[0].split())
    except:
        print("Impossible.")
        return
        
    lines = data[1:1+n]
    
    result = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append(" " * k)
            continue
            
        current_len = len(line)
        if current_len > k:
            print("Impossible.")
            return
            
        total_spaces = k - len(stripped)
        left_spaces = total_spaces // 2
        
        if total_spaces % 2 == 1:
            if left_spaces + 1 <= total_spaces - left_spaces:
                left_spaces += 1
                
        right_spaces = total_spaces - left_spaces
        
        if left_spaces > right_spaces:
            print("Impossible.")
            return
            
        if left_spaces + 1 <= right_spaces - 1:
            print("Impossible.")
            return
            
        formatted_line = " " * left_spaces + stripped + " " * right_spaces
        result.append(formatted_line)
    
    with open("OUTPUT.TXT", "w") as f:
        for line in result:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
