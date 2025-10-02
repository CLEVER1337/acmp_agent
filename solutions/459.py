
def main():
    with open('INPUT.TXT', 'r') as f:
        path = f.read().strip()
    
    directions = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}
    reverse_path = ''.join(directions[step] for step in reversed(path))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(reverse_path)

if __name__ == '__main__':
    main()
