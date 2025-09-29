
def main():
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())
    
    box1 = sorted([a1, b1, c1])
    box2 = sorted([a2, b2, c2])
    
    if box1 == box2:
        print("Boxes are equal")
    elif box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]:
        print("The first box is smaller than the second one")
    elif box2[0] <= box1[0] and box2[1] <= box1[1] and box2[2] <= box1[2]:
        print("The first box is larger than the second one")
    else:
        print("Boxes are incomparable")

if __name__ == "__main__":
    main()
