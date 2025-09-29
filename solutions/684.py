
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.readline().split()
    
    start, end = data[0], data[1]
    
    start_col = ord(start[0]) - ord('a')
    start_row = int(start[1]) - 1
    
    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1
    
    if end_row <= start_row:
        print("NO")
        return
    
    if abs(end_col - start_col) > end_row - start_row:
        print("NO")
        return
    
    if (start_col + start_row) % 2 != 0 or (end_col + end_row) % 2 != 0:
        print("NO")
        return
    
    print("YES")

if __name__ == "__main__":
    main()
