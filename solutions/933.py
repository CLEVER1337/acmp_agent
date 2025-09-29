
def main():
    with open('INPUT.TXT', 'r') as f:
        A, B, C, T = map(int, f.readline().split())
    
    if T <= A:
        cost = T * B
    else:
        cost = A * B + (T - A) * C
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(cost))

if __name__ == '__main__':
    main()
