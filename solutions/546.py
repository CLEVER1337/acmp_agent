
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    sheets = (n + 3) // 4
    commands = []
    
    for sheet in range(1, sheets + 1):
        first_page = 2 * sheets - 2 * (sheet - 1)
        second_page = 2 * sheet - 1
        
        # Лицевая сторона
        if first_page <= n or second_page <= n:
            left = first_page if first_page <= n else 0
            right = second_page if second_page <= n else 0
            commands.append(f"{sheet} 1 {left} {right}")
        
        # Обратная сторона
        third_page = 2 * sheet
        fourth_page = 2 * sheets - 2 * sheet + 1
        
        if third_page <= n or fourth_page <= n:
            left = third_page if third_page <= n else 0
            right = fourth_page if fourth_page <= n else 0
            commands.append(f"{sheet} 2 {left} {right}")
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(commands))

if __name__ == '__main__':
    main()
