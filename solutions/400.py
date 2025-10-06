
def main():
    tiles = []
    for _ in range(6):
        w, h = map(int, input().split())
        if w > h:
            w, h = h, w
        tiles.append((w, h))
    
    tiles.sort()
    
    if tiles[0] == tiles[1] and tiles[2] == tiles[3] and tiles[4] == tiles[5]:
        a, b = tiles[0]
        c, d = tiles[2]
        e, f = tiles[4]
        
        if (a == c and b == e and d == f) or (a == c and b == f and d == e) or \
           (a == d and b == e and c == f) or (a == d and b == f and c == e) or \
           (a == e and b == c and d == f) or (a == e and b == d and c == f) or \
           (a == f and b == c and d == e) or (a == f and b == d and c == e):
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
