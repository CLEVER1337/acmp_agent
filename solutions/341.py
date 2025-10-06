
def main():
    n = int(input().strip())
    if n == 1:
        print(0)
        return
        
    a_prev = 0
    for i in range(2, n + 1):
        digits_prev = set(str(a_prev))
        candidate = a_prev + 1
        while True:
            digits_candidate = set(str(candidate))
            if not digits_candidate.intersection(digits_prev):
                a_prev = candidate
                break
            candidate += 1
            
    print(a_prev)

if __name__ == "__main__":
    main()
