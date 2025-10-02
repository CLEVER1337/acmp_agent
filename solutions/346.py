
def main():
    with open("INPUT.TXT", "r") as f:
        a, b, c = map(int, f.readline().split())
    
    def get_permutations(n):
        digits = list(str(n))
        from itertools import permutations
        perms = set()
        for p in permutations(digits):
            num_str = ''.join(p)
            if num_str[0] != '0' or len(num_str) == 1:
                perms.add(int(num_str))
        return sorted(perms)
    
    a_perms = get_permutations(a)
    b_perms = get_permutations(b)
    
    found = False
    result_x = None
    result_y = None
    
    for x in a_perms:
        target = c - x
        if target in b_perms:
            found = True
            result_x = x
            result_y = target
            break
    
    with open("OUTPUT.TXT", "w") as f:
        if found:
            f.write("YES\n")
            f.write(f"{result_x} {result_y}\n")
        else:
            f.write("NO\n")

if __name__ == "__main__":
    main()
