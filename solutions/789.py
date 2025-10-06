
def is_valid(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            return False
    return True

def main():
    n = int(input().strip())
    count = 0
    num = 0
    while count < n:
        num += 1
        if is_valid(num):
            count += 1
    print(num)

if __name__ == '__main__':
    main()
