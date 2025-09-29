
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        dictionary = []
        for _ in range(n):
            dictionary.append(f.readline().strip())
        letters = f.readline().strip()
    
    from collections import Counter
    letters_counter = Counter(letters)
    count = 0
    
    for word in dictionary:
        word_counter = Counter(word)
        can_form = True
        for char in word_counter:
            if word_counter[char] > letters_counter.get(char, 0):
                can_form = False
                break
        if can_form:
            count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
