
def main():
    with open('INPUT.TXT', 'r') as f:
        n = f.readline().strip()
    
    s = ""
    pos = 0
    target = str(n)
    i = 1
    
    while True:
        num_str = str(i)
        s += num_str
        if len(s) >= len(target):
            found_pos = s.find(target)
            if found_pos != -1:
                pos += found_pos + 1
                break
        pos += len(num_str)
        i += 1
        
        if len(s) > 100000:
            s = s[-len(target)*2:]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(pos))

if __name__ == "__main__":
    main()
