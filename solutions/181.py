
def main():
    rules = {}
    directions = ['N', 'S', 'W', 'E', 'U', 'D']
    
    with open('INPUT.TXT', 'r') as f:
        for i in range(6):
            rule_str = f.readline().strip()
            rules[directions[i]] = rule_str
        
        command_line = f.readline().split()
        direction = command_line[0]
        M = int(command_line[1])
    
    memo = {}
    
    def count_moves(cmd_dir, m):
        if m == 1:
            return 1
        
        if (cmd_dir, m) in memo:
            return memo[(cmd_dir, m)]
        
        rule = rules[cmd_dir]
        total = 1
        
        for char in rule:
            total += count_moves(char, m - 1)
        
        memo[(cmd_dir, m)] = total
        return total
    
    result = count_moves(direction, M)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
