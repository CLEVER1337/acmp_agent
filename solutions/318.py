
def main():
    n = int(input().strip())
    count_ones = bin(n).count('1')
    next_num = n + 1
    while True:
        if bin(next_num).count('1') == count_ones:
            print(next_num)
            return
        next_num += 1

if __name__ == '__main__':
    main()
