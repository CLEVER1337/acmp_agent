
def main():
    with open("INPUT.TXT", "r") as f:
        N, M, F, L = map(int, f.readline().split())
    
    both = M + F + L - N
    math_only = M - both
    physics_only = F - both
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(f"{both} {math_only} {physics_only}")

if __name__ == "__main__":
    main()
