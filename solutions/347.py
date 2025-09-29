
def main():
    with open('INPUT.TXT', 'r') as f:
        numbers = list(map(int, f.readline().split()))
    
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    freq = sorted(counts.values(), reverse=True)
    unique = sorted(counts.keys())
    
    if freq[0] == 5:
        result = "Impossible"
    elif freq[0] == 4:
        result = "Four of a Kind"
    elif freq[0] == 3 and freq[1] == 2:
        result = "Full House"
    elif len(unique) == 5 and max(unique) - min(unique) == 4:
        result = "Straight"
    elif freq[0] == 3:
        result = "Three of a Kind"
    elif freq[0] == 2 and freq[1] == 2:
        result = "Two Pairs"
    elif freq[0] == 2:
        result = "One Pair"
    else:
        result = "Nothing"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
