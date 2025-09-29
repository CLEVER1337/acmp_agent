
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
        tw, th, w, h = map(int, data)
    
    if (w % tw == 0 and h % th == 0) or (w % th == 0 and h % tw == 0):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
