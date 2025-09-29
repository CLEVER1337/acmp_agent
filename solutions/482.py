
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    pos = 0
    k = 1
    
    while True:
        group = ''
        for i in range(1, k + 1):
            group += str(i)
        
        group_length = len(group)
        
        if pos + group_length >= N:
            digit_index = N - pos - 1
            print(group[digit_index])
            break
            
        pos += group_length
        k += 1

if __name__ == '__main__':
    main()
