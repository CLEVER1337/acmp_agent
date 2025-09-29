
def main():
    with open('INPUT.TXT', 'r') as f:
        K = int(f.read().strip())
    
    initial = ['G', 'C', 'V']
    
    for day in range(K):
        # Утро: Маша меняет правый и центральный
        initial[1], initial[2] = initial[2], initial[1]
        
        # Вечер: Таня меняет левый и центральный
        initial[0], initial[1] = initial[1], initial[0]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(''.join(initial))

if __name__ == '__main__':
    main()
