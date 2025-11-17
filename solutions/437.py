
import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    try:
        numbers = list(map(int, data))
    except Exception:
        # In case of invalid input, output nothing
        return

    freq_counter = Counter(numbers)
    sorted_freq = sorted(freq_counter.items(), key=lambda x: (-x[1], x[0]))
    
    for number, count in sorted_freq:
        if count == 1:
            print(f"{number} appears 1 time")
        else:
            print(f"{number} appears {count} times")

if __name__ == "__main__":
    main()
