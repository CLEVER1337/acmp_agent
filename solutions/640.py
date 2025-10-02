
def read_image(f, n, m):
    return [f.readline().strip() for _ in range(n)]

def rotate_90(image):
    return [''.join(image[i][j] for i in range(len(image)-1, -1, -1)) for j in range(len(image[0]))]

def flip_vertical(image):
    return [row[::-1] for row in image]

def generate_variants(image):
    variants = []
    current = image
    for _ in range(4):
        variants.append(current)
        variants.append(flip_vertical(current))
        current = rotate_90(current)
    return variants

def main():
    with open('INPUT.TXT', 'r') as f:
        n1, m1 = map(int, f.readline().split())
        img1 = read_image(f, n1, m1)
        n2, m2 = map(int, f.readline().split())
        img2 = read_image(f, n2, m2)
    
    if n1 != n2 or m1 != m2:
        print("No")
        return
    
    variants = generate_variants(img1)
    for variant in variants:
        if variant == img2:
            print("Yes")
            return
    
    print("No")

if __name__ == "__main__":
    main()
