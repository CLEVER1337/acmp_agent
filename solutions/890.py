
def main():
    data = []
    for _ in range(2):
        line = input().split()
        data.append(tuple(map(int, line)))
    
    (x11, y11, z11, x12, y12, z12) = data[0]
    (x21, y21, z21, x22, y22, z22) = data[1]
    
    def volume(x1, y1, z1, x2, y2, z2):
        return abs(x2 - x1) * abs(y2 - y1) * abs(z2 - z1)
    
    vol1 = volume(x11, y11, z11, x12, y12, z12)
    vol2 = volume(x21, y21, z21, x22, y22, z22)
    
    def intersection_volume():
        x1_overlap = max(min(x11, x12), min(x21, x22))
        x2_overlap = min(max(x11, x12), max(x21, x22))
        x_overlap = max(0, x2_overlap - x1_overlap)
        
        y1_overlap = max(min(y11, y12), min(y21, y22))
        y2_overlap = min(max(y11, y12), max(y21, y22))
        y_overlap = max(0, y2_overlap - y1_overlap)
        
        z1_overlap = max(min(z11, z12), min(z21, z22))
        z2_overlap = min(max(z11, z12), max(z21, z22))
        z_overlap = max(0, z2_overlap - z1_overlap)
        
        return x_overlap * y_overlap * z_overlap
    
    inter_vol = intersection_volume()
    total_vol = vol1 + vol2 - inter_vol
    print(total_vol)

if __name__ == "__main__":
    main()
