
def main():
    with open('INPUT.TXT', 'r') as f:
        total_sum = int(f.read().strip())
    
    goals = 0
    while goals * (goals + 1) <= total_sum:
        goals += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(goals))

if __name__ == '__main__':
    main()
