
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        s = f.readline().strip()
    
    buttons = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    
    for i in range(len(s)):
        if dp[i] == 0:
            continue
        current_char = s[i]
        current_button = buttons[current_char]
        count_on_button = 4 if current_button in '79' else 3
        
        j = i
        while j < len(s) and buttons[s[j]] == current_button:
            press_count = j - i + 1
            letter_index = (press_count - 1) % count_on_button
            if letter_index == count_on_button - 1:
                if j + 1 - i <= n:
                    dp[j + 1] += dp[i]
            j += 1
        
        if i + 1 <= len(s):
            dp[i + 1] += dp[i]
    
    print(dp[len(s)])

if __name__ == '__main__':
    main()
