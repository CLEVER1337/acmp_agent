
def main():
    import sys
    data = sys.stdin.read().split()
    F = int(data[0])
    P = int(data[1])
    
    low, high = 1, 2 * 10**9
    
    def is_possible(S):
        bottles = S // F
        money = S % F
        for day in range(4):
            if bottles == 0:
                return False
            money += bottles * P
            bottles = money // F
            money %= F
        return bottles >= 1 and money == 0
    
    while low < high:
        mid = (low + high) // 2
        if is_possible(mid):
            high = mid
        else:
            low = mid + 1
            
    print(low)

if __name__ == "__main__":
    main()
