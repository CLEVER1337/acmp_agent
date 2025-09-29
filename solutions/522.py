
def main():
    with open("INPUT.TXT", "r") as f:
        m, n = map(int, f.readline().split())
        arr1 = list(map(int, f.readline().split()))
        arr2 = list(map(int, f.readline().split()))
    
    set1 = set(arr1)
    set2 = set(arr2)
    
    result = 1 if set1 == set2 else 0
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
