
def generate(n, s='', balance=0, stack=[]):
    if len(s) == n:
        if balance == 0 and not stack:
            print(s)
        return
    
    for bracket in ['()', '[]']:
        open_bracket, close_bracket = bracket[0], bracket[1]
        
        if balance < n // 2:
            generate(n, s + open_bracket, balance + 1, stack + [open_bracket])
        
        if balance > 0 and stack and stack[-1] == open_bracket:
            generate(n, s + close_bracket, balance - 1, stack[:-1])

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    generate(n)

if __name__ == '__main__':
    main()
