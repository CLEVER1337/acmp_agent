
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    U = int(data[0])
    H = int(data[1])
    T = int(data[2])
    L = int(data[3])
    N = int(data[4])
    X = list(map(int, data[5:5+N]))
    
    total_scroll_steps = (L - U + T - 1) // T
    if L <= U:
        total_scroll_steps = 0
    
    best_ans = float('inf')
    
    for cursor_start in range(0, U - H + 1):
        count = 0
        for step in range(total_scroll_steps + 1):
            scroll_offset = step * T
            cursor_top = cursor_start
            cursor_bottom = cursor_start + H - 1
            
            for i in range(N):
                line_pos_in_table = X[i]
                line_pos_on_screen = line_pos_in_table - scroll_offset
                
                if cursor_top <= line_pos_on_screen <= cursor_bottom:
                    count += 1
        
        if count < best_ans:
            best_ans = count
    
    print(best_ans)

if __name__ == "__main__":
    main()
