
def main():
    with open('INPUT.TXT', 'r') as f:
        m, n = map(int, f.read().split())
    
    commands = []
    x, y = 0, 0
    direction = 0  # 0: up, 1: right, 2: down, 3: left
    visited = set()
    
    def move(distance):
        nonlocal x, y
        if direction == 0:
            y += distance
        elif direction == 1:
            x += distance
        elif direction == 2:
            y -= distance
        elif direction == 3:
            x -= distance
    
    def turn_right():
        nonlocal direction
        direction = (direction + 1) % 4
    
    def turn_left():
        nonlocal direction
        direction = (direction - 1) % 4
    
    steps = []
    while True:
        if direction == 0:  # up
            max_move = n - 1 - y
        elif direction == 1:  # right
            max_move = m - 1 - x
        elif direction == 2:  # down
            max_move = y
        else:  # left
            max_move = x
        
        if max_move <= 0:
            break
        
        steps.append(max_move)
        move(max_move)
        
        turn_right()
        if direction == 0 and y >= n - 1:
            break
        elif direction == 1 and x >= m - 1:
            break
        elif direction == 2 and y <= 0:
            break
        elif direction == 3 and x <= 0:
            break
    
    commands = []
    for i, step in enumerate(steps):
        commands.append(f'f {step}')
        if i < len(steps) - 1:
            commands.append('r')
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f'{len(commands)}\n')
        f.write('\n'.join(commands))

if __name__ == '__main__':
    main()
