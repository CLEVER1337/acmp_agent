
import sys
import re

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("Everything is going to be OK.")
        return
        
    n, m = map(int, data[0].split())
    dictionary = set()
    
    for i in range(1, 1 + n):
        dictionary.add(data[i].lower())
    
    text = ' '.join(data[1 + n:1 + n + m])
    text_clean = re.sub(r'[^a-zA-Z\s]', ' ', text.lower())
    words_in_text = set(re.findall(r'\b[a-z]+\b', text_clean))
    
    unknown_words = words_in_text - dictionary
    missing_words = dictionary - words_in_text
    
    if unknown_words:
        print("Some words from the text are unknown.")
    elif missing_words:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == "__main__":
    main()
