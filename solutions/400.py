
def main():
    tiles = []
    with open('INPUT.TXT', 'r') as f:
        for _ in range(6):
            w, h = map(int, f.readline().split())
            tiles.append((min(w, h), max(w, h)))
    
    tiles.sort()
    
    if tiles[0][0] == tiles[1][0] == tiles[2][0] == tiles[3][0] and \
       tiles[0][1] == tiles[1][1] and tiles[2][1] == tiles[3][1] and \
       tiles[4][0] == tiles[5][0] and tiles[4][1] == tiles[5][1] and \
       tiles[0][0] == tiles[4][0] and tiles[0][1] == tiles[4][1] and tiles[2][1] == tiles[5][1]:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
