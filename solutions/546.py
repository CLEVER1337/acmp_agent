
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    sheets = (n + 3) // 4
    commands = []
    
    for sheet in range(1, sheets + 1):
        first_page = 4 * (sheet - 1) + 1
        last_page = 4 * sheet
        
        page1 = last_page - 1 if last_page - 1 <= n else 0
        page2 = first_page if first_page <= n else 0
        page3 = first_page + 1 if first_page + 1 <= n else 0
        page4 = last_page - 2 if last_page - 2 <= n else 0
        
        if page1 != 0 or page2 != 0:
            commands.append(f"{sheet} 1 {page1} {page2}")
        
        if page3 != 0 or page4 != 0:
            commands.append(f"{sheet} 2 {page3} {page4}")
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(commands))

if __name__ == "__main__":
    main()
