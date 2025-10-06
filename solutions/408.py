
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("Impossible.")
        return
        
    first_line = data[0].split()
    if len(first_line) < 2:
        print("Impossible.")
        return
        
    try:
        K = int(first_line[0])
        N = int(first_line[1])
    except:
        print("Impossible.")
        return
        
    lines = []
    for i in range(1, 1 + N):
        if i >= len(data):
            break
        line = data[i].rstrip('\n')
        lines.append(line)
        
    if len(lines) != N:
        print("Impossible.")
        return
        
    result_lines = []
    for line in lines:
        stripped = line.rstrip()
        if len(stripped) > K:
            print("Impossible.")
            return
            
        total_spaces_needed = K - len(stripped)
        left_spaces = (total_spaces_needed + 1) // 2
        
        if total_spaces_needed % 2 == 1:
            if left_spaces <= total_spaces_needed - left_spaces:
                if left_spaces + 1 > total_spaces_needed - left_spaces - 1:
                    left_final = left_spaces
                else:
                    left_final = left_spaces + 1
            else:
                left_final = left_spaces
        else:
            left_final = total_spaces_needed // 2
            
        right_final = total_spaces_needed - left_final
        
        if left_final > right_final:
            print("Impossible.")
            return
            
        formatted_line = ' ' * left_final + stripped + ' ' * right_final
        result_lines.append(formatted_line)
        
    for line in result_lines:
        print(line)

if __name__ == "__main__":
    main()
