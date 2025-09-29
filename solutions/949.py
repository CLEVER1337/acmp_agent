
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        n = int(data[0])
        a_n = int(data[1])
        a_n1 = int(data[2])
    
    if n == 1:
        a1 = a_n
        a2 = a_n1
    elif n == 2:
        a1 = a_n1 - a_n
        a2 = a_n
    else:
        f_prev = 1
        f_curr = 1
        for i in range(3, n):
            f_next = f_prev + f_curr
            f_prev, f_curr = f_curr, f_next
        
        a1 = (a_n1 - a_n * f_prev) // f_curr
        a2 = (a_n - a1 * f_prev) // f_curr
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{a1} {a2}")

if __name__ == "__main__":
    main()
