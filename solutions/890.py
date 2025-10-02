
def main():
    with open('INPUT.TXT', 'r') as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
    
    coords1 = list(map(int, line1.split()))
    coords2 = list(map(int, line2.split()))
    
    def volume(c):
        return abs(c[3] - c[0]) * abs(c[4] - c[1]) * abs(c[5] - c[2])
    
    def intersection(c1, c2):
        x_overlap = max(0, min(c1[3], c2[3]) - max(c1[0], c2[0]))
        y_overlap = max(0, min(c1[4], c2[4]) - max(c1[1], c2[1]))
        z_overlap = max(0, min(c1[5], c2[5]) - max(c1[2], c2[2]))
        return x_overlap * y_overlap * z_overlap
    
    v1 = volume(coords1)
    v2 = volume(coords2)
    inter_vol = intersection(coords1, coords2)
    
    total_volume = v1 + v2 - inter_vol
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(total_volume))

if __name__ == '__main__':
    main()
