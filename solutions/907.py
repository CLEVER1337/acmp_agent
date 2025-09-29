
def main():
    with open('INPUT.TXT', 'r') as f:
        W, H, R = map(int, f.readline().split())
    
    if R * 2 <= min(W, H):
        result = "YES"
    else:
        result = "NO"
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
