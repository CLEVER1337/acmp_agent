
def count_groups(n):
    if n < 3:
        return 0
    if n == 3:
        return 1
    
    if n % 2 == 0:
        return count_groups(n // 2) + count_groups(n // 2)
    else:
        return count_groups(n // 2) + count_groups(n // 2 + 1)

def main():
    n = int(input().strip())
    print(count_groups(n))

if __name__ == "__main__":
    main()
