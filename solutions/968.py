
def main():
    with open('INPUT.TXT', 'r') as f:
        SA, SB = f.read().splitlines()
    
    n = len(SA)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_to_pos = {char: idx for idx, char in enumerate(alphabet)}
    
    def dist(c1, c2):
        pos1 = char_to_pos[c1]
        pos2 = char_to_pos[c2]
        diff = abs(pos1 - pos2)
        return min(diff, 26 - diff)
    
    total = 0
    for k in range(n):
        shift_SA = SA[k:] + SA[:k]
        current_sum = 0
        for i in range(n):
            current_sum += dist(shift_SA[i], SB[i])
        total += current_sum
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total))

if __name__ == '__main__':
    main()
