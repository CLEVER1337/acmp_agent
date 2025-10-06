
def main():
    n = int(input().strip())
    total_length = 2**26 - 1
    result = find_char(n, total_length, 26)
    print(result)

def find_char(pos, total_len, step):
    if step == 1:
        return 'a'
    
    half_len = (total_len - 1) // 2
    if pos == half_len + 1:
        return chr(ord('a') + step - 1)
    elif pos <= half_len:
        return find_char(pos, half_len, step - 1)
    else:
        return find_char(pos - half_len - 1, half_len, step - 1)

if __name__ == "__main__":
    main()
