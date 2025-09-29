
def main():
    import sys
    from collections import Counter
    
    data = sys.stdin.read().splitlines()
    if not data:
        print("0\n0\n0")
        return
        
    target_word = data[0].strip()
    target_counter = Counter(target_word)
    
    idx = 1
    
    n1 = int(data[idx]); idx += 1
    player1_words = []
    for i in range(n1):
        word = data[idx].strip(); idx += 1
        word_counter = Counter(word)
        valid = True
        for char, count in word_counter.items():
            if count > target_counter.get(char, 0):
                valid = False
                break
        if valid:
            player1_words.append(word)
            
    n2 = int(data[idx]); idx += 1
    player2_words = []
    for i in range(n2):
        word = data[idx].strip(); idx += 1
        word_counter = Counter(word)
        valid = True
        for char, count in word_counter.items():
            if count > target_counter.get(char, 0):
                valid = False
                break
        if valid:
            player2_words.append(word)
            
    valid_words1 = set(player1_words)
    valid_words2 = set(player2_words)
    
    common_words = valid_words1 & valid_words2
    only1_words = valid_words1 - common_words
    only2_words = valid_words2 - common_words
    
    common_count = len(common_words)
    count1 = len(only1_words)
    count2 = len(only2_words)
    
    # Case 1: Both play optimally
    if common_count % 2 == 0:
        if count1 > count2:
            result1 = 1
        elif count2 > count1:
            result1 = 2
        else:
            result1 = 0
    else:
        if count1 >= count2:
            result1 = 1
        elif count2 == count1 + 1:
            result1 = 0
        else:
            result1 = 2
            
    # Case 2: First plays optimally, second plays worst
    if common_count % 2 == 0:
        if count1 > count2:
            result2 = 1
        elif count2 > count1:
            result2 = 2
        else:
            result2 = 0
    else:
        if count1 > count2:
            result2 = 1
        elif count1 == count2:
            result2 = 1
        else:
            result2 = 2
            
    # Case 3: First throws (submits)
    if common_count % 2 == 0:
        if count1 >= count2:
            result3 = 2
        else:
            result3 = 2
    else:
        if count1 > count2:
            result3 = 2
        elif count1 == count2:
            result3 = 2
        else:
            result3 = 2
            
    print(f"{result1}\n{result2}\n{result3}")

if __name__ == "__main__":
    main()
