
with open('INPUT.TXT', 'r') as f:
    data = f.readlines()
    if not data:
        print("Impossible.")
        exit()
    
    first_line = data[0].split()
    if len(first_line) < 2:
        print("Impossible.")
        exit()
        
    K = int(first_line[0])
    N = int(first_line[1])
    
    lines = [line.rstrip('\n').rstrip('\r') for line in data[1:1+N]]
    
    formatted_lines = []
    for line in lines:
        stripped = line.strip()
        if len(stripped) > K:
            print("Impossible.")
            exit()
            
        total_spaces = K - len(stripped)
        left_spaces = total_spaces // 2
        right_spaces = total_spaces - left_spaces
        
        if left_spaces > right_spaces:
            left_spaces, right_spaces = right_spaces, left_spaces
            
        if left_spaces + 1 <= right_spaces - 1:
            left_spaces += 1
            right_spaces -= 1
            
        if left_spaces > right_spaces:
            print("Impossible.")
            exit()
            
        formatted_line = ' ' * left_spaces + stripped + ' ' * right_spaces
        formatted_lines.append(formatted_line)
        
    with open('OUTPUT.TXT', 'w') as out:
        for line in formatted_lines:
            out.write(line + '\n')
