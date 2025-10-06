
def main():
    n = int(input().strip())
    sheets = (n + 3) // 4
    commands = []
    
    for sheet in range(1, sheets + 1):
        page1 = 2 * sheets - 2 * (sheet - 1)
        page2 = 2 * (sheet - 1) + 1
        page3 = page2 + 1
        page4 = page1 - 1
        
        if page1 <= n:
            left1 = page1
        else:
            left1 = 0
            
        if page2 <= n:
            right1 = page2
        else:
            right1 = 0
            
        if page3 <= n:
            left2 = page3
        else:
            left2 = 0
            
        if page4 <= n:
            right2 = page4
        else:
            right2 = 0
            
        if left1 != 0 or right1 != 0:
            commands.append(f"{sheet} 1 {left1} {right1}")
        if left2 != 0 or right2 != 0:
            commands.append(f"{sheet} 2 {left2} {right2}")
    
    with open("OUTPUT.TXT", "w") as f:
        for cmd in commands:
            f.write(cmd + "\n")

if __name__ == "__main__":
    main()
