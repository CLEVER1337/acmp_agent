
def main():
    with open("INPUT.TXT", "r") as f:
        a, b, c = f.readline().split()
    
    def get_permutations(num_str):
        if len(num_str) == 0:
            return ['']
        digits = list(num_str)
        perms = set()
        from itertools import permutations
        for p in permutations(digits):
            perm_str = ''.join(p)
            if perm_str[0] != '0' or len(perm_str) == 1:
                perms.add(perm_str)
        return sorted([int(x) for x in perms])
    
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
            f.write(f"{result_x} {result_y}")
        else:
            f.write("NO")

if __name__ == "__main__":
    main()
