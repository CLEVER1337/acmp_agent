
def main():
    import sys
    from collections import Counter
    
    data = sys.stdin.read().splitlines()
    long_word = data[0].strip()
    long_count = Counter(long_word)
    
    def is_valid(word):
        wc = Counter(word)
        for c in wc:
            if wc[c] > long_count.get(c, 0):
                return False
        return True
    
    idx = 1
    n1 = int(data[idx]); idx += 1
    words1 = []
    for i in range(n1):
        word = data[idx].strip(); idx += 1
        if is_valid(word):
            words1.append(word)
    
    n2 = int(data[idx]); idx += 1
    words2 = []
    for i in range(n2):
        word = data[idx].strip(); idx += 1
        if is_valid(word):
            words2.append(word)
    
    words1 = list(set(words1))
    words2 = list(set(words2))
    
    common_words = set(words1) & set(words2)
    only1 = set(words1) - common_words
    only2 = set(words2) - common_words
    
    total_common = len(common_words)
    total_only1 = len(only1)
    total_only2 = len(only2)
    
    def optimal_play():
        if total_only1 > total_only2:
            return 1
        elif total_only2 > total_only1:
            return 2
        else:
            if total_common % 2 == 1:
                return 1
            else:
                return 0
    
    def first_sabotage():
        if total_only1 == 0 and total_only2 == 0:
            if total_common == 0:
                return 0
            else:
                return 2
        
        if total_only1 >= total_only2:
            if total_only1 > total_only2:
                return 2
            else:
                if total_common % 2 == 0:
                    return 2
                else:
                    return 2
        else:
            if total_only2 > total_only1 + total_common:
                return 2
            else:
                moves = total_only1 + total_common
                if moves < total_only2:
                    return 2
                remaining = moves - total_only2
                if remaining % 2 == 1:
                    return 1
                else:
                    return 2
    
    def second_sabotage():
        if total_only1 == 0 and total_only2 == 0:
            if total_common == 0:
                return 0
            else:
                return 1
        
        if total_only2 >= total_only1:
            if total_only2 > total_only1:
                return 1
            else:
                if total_common % 2 == 0:
                    return 1
                else:
                    return 1
        else:
            if total_only1 > total_only2 + total_common:
                return 1
            else:
                moves = total_only2 + total_common
                if moves < total_only1:
                    return 1
                remaining = moves - total_only1
                if remaining % 2 == 1:
                    return 2
                else:
                    return 1
    
    res1 = optimal_play()
    res2 = first_sabotage()
    res3 = second_sabotage()
    
    print(res1)
    print(res2)
    print(res3)

if __name__ == "__main__":
    main()
