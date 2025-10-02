
def main():
    with open("INPUT.TXT", "r") as f:
        F, P = map(int, f.readline().split())
    
    left, right = 0, 2 * 10**9
    result = right
    
    def check(initial):
        bottles = initial // F
        change = initial % F
        for day in range(4):
            if bottles == 0:
                return False
            returned = bottles * P
            total = returned + change
            bottles = total // F
            change = total % F
        return bottles == 1 and change == 0
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
            
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
