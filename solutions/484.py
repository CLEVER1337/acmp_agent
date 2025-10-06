
def main():
    S = int(input().strip())
    result = []
    current = S
    while current > 0:
        result.append(str(current))
        if current == 1:
            break
        if current % 2 == 0:
            current = current // 2
        else:
            current = (current - 1) // 2
    print(' '.join(result))

if __name__ == '__main__':
    main()
