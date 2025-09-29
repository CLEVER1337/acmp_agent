
import re

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    query = lines[0].strip()
    text = ''.join(lines[1:])
    
    query_words = query.split()
    pattern = r'\s+'.join(re.escape(word) for word in query_words)
    
    def replace_func(match):
        return '@' + match.group(0)
    
    result = re.sub(pattern, replace_func, text, flags=re.IGNORECASE)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
