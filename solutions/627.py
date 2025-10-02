
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print("0\n0\n0")
        return
        
    target_word = data[0].strip()
    target_count = [0] * 26
    for c in target_word:
        idx = ord(c) - ord('a')
        if 0 <= idx < 26:
            target_count[idx] += 1

    def can_form(word):
        if not word:
            return False
        count = [0] * 26
        for c in word:
            idx = ord(c) - ord('a')
            if 0 <= idx < 26:
                count[idx] += 1
        for i in range(26):
            if count[i] > target_count[i]:
                return False
        return True

    n1 = int(data[1].strip())
    player1_words = []
    for i in range(2, 2 + n1):
        word = data[i].strip()
        if can_form(word):
            player1_words.append(word)

    n2 = int(data[2 + n1].strip())
    player2_words = []
    for i in range(3 + n1, 3 + n1 + n2):
        word = data[i].strip()
        if can_form(word):
            player2_words.append(word)

    common_words = set(player1_words) & set(player2_words)
    p1_unique = len(player1_words) - len(common_words)
    p2_unique = len(player2_words) - len(common_words)
    common_count = len(common_words)

    def both_optimal():
        if p1_unique > p2_unique:
            return 1
        elif p2_unique > p1_unique:
            return 2
        else:
            if common_count % 2 == 1:
                return 1
            else:
                return 0

    def first_optimal_second_worst():
        if p1_unique > p2_unique + common_count:
            return 1
        elif p2_unique > p1_unique:
            return 2
        else:
            remaining = common_count - max(0, p2_unique - p1_unique)
            if remaining % 2 == 1:
                return 1
            else:
                return 0

    def first_sandbagging():
        if p2_unique > p1_unique + common_count:
            return 2
        elif p1_unique > p2_unique:
            return 1
        else:
            remaining = common_count - max(0, p1_unique - p2_unique)
            if remaining % 2 == 1:
                return 2
            else:
                return 0

    result1 = both_optimal()
    result2 = first_optimal_second_worst()
    result3 = first_sandbagging()
    
    print(result1)
    print(result2)
    print(result3)

if __name__ == "__main__":
    main()
