
def main():
    with open("INPUT.TXT", "r") as f:
        N, A, B = map(int, f.read().split())
    
    result = 0
    for red_in_boxes in range(min(A, N) + 1):
        for blue_in_boxes in range(min(B, N) + 1):
            if red_in_boxes + blue_in_boxes <= N:
                ways_red = comb(A, red_in_boxes)
                ways_blue = comb(B, blue_in_boxes)
                ways_distribute_red = stirling(red_in_boxes, N - blue_in_boxes)
                ways_distribute_blue = stirling(blue_in_boxes, N - red_in_boxes)
                result += ways_red * ways_blue * ways_distribute_red * ways_distribute_blue
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

def comb(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result

def stirling(k, n):
    if k == 0:
        return 1 if n >= 0 else 0
    total = 0
    for j in range(k + 1):
        sign = 1 if j % 2 == 0 else -1
        total += sign * comb(k, j) * (k - j) ** n
    return total // factorial(k)

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    main()
