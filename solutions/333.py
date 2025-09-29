
def main():
    with open("INPUT.TXT", "r") as f:
        A, B, C = f.readline().split()
    
    set_A = set(A)
    set_B = set(B)
    set_C = set(C)
    
    common_digits = sorted(set_A & set_B & set_C)
    count = len(common_digits)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{count}\n")
        if common_digits:
            f.write(" ".join(common_digits))

if __name__ == "__main__":
    main()
