
def main():
    with open('INPUT.TXT', 'r') as f:
        SA, SB = f.read().splitlines()
    
    n = len(SA)
    total = 0
    
    for k in range(n):
        shifted_SB = SB[k:] + SB[:k]
        for i in range(n):
            a = ord(SA[i]) - ord('a')
            b = ord(shifted_SB[i]) - ord('a')
            diff = abs(a - b)
            total += min(diff, 26 - diff)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total))

if __name__ == '__main__':
    main()
