
def main():
    tiles = []
    with open('INPUT.TXT', 'r') as f:
        for line in f:
            w, h = map(int, line.split())
            tiles.append((min(w, h), max(w, h)))
    
    counts = {}
    for tile in tiles:
        key = tuple(tile)
        counts[key] = counts.get(key, 0) + 1
    
    if len(counts) > 3:
        print("IMPOSSIBLE")
        return
    
    sides = list(counts.keys())
    if len(sides) == 1:
        if counts[sides[0]] == 6:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")
    elif len(sides) == 2:
        a, count_a = sides[0], counts[sides[0]]
        b, count_b = sides[1], counts[sides[1]]
        
        if (count_a == 2 and count_b == 4) or (count_a == 4 and count_b == 2):
            if (a[0] == b[0] and a[1] == b[1]) or (a[0] == b[0] and a[1] == b[0]) or (a[0] == b[1] and a[1] == b[1]):
                print("POSSIBLE")
            else:
                print("IMPOSSIBLE")
        else:
            print("IMPOSSIBLE")
    elif len(sides) == 3:
        a, count_a = sides[0], counts[sides[0]]
        b, count_b = sides[1], counts[sides[1]]
        c, count_c = sides[2], counts[sides[2]]
        
        if count_a == 2 and count_b == 2 and count_c == 2:
            dimensions = set()
            for side in sides:
                dimensions.add(side[0])
                dimensions.add(side[1])
            
            if len(dimensions) == 3:
                sorted_dims = sorted(dimensions)
                if (sorted_dims[0], sorted_dims[1]) in sides and \
                   (sorted_dims[0], sorted_dims[2]) in sides and \
                   (sorted_dims[1], sorted_dims[2]) in sides:
                    print("POSSIBLE")
                else:
                    print("IMPOSSIBLE")
            else:
                print("IMPOSSIBLE")
        else:
            print("IMPOSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
