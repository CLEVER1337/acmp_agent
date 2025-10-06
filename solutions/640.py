
def read_image():
    n, m = map(int, input().split())
    image = []
    for _ in range(n):
        image.append(input().strip())
    return image

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
    image1 = read_image()
    image2 = read_image()
    
    variants1 = generate_variants(image1)
    
    for variant in variants1:
        if variant == image2:
            print("Yes")
            return
    
    print("No")

if __name__ == "__main__":
    main()
