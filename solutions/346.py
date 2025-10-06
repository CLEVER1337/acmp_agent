
def main():
    a, b, c = input().split()
    
    def get_permutations(s):
        from itertools import permutations
        perms = set()
        for p in permutations(s):
            if p[0] != '0':
                perms.add(''.join(p))
        return sorted(perms)
    
    a_perms = get_permutations(a)
    b_perms = get_permutations(b)
    
    for x in a_perms:
        rem = str(int(c) - int(x))
        if len(rem) != len(b):
            continue
        if ''.join(sorted(rem)) == ''.join(sorted(b)):
            y = rem
            print("YES")
            print(x, y)
            return
    
    print("NO")

if __name__ == "__main__":
    main()
