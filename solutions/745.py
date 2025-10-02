
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        W = int(data[0])
        H = int(data[1])
        x = int(data[2])
        y = int(data[3])
        a = int(data[4])
        b = int(data[5])
    
    scale_x = (W * 100) / a
    scale_y = (H * 100) / b
    
    fixed_point_x = (x * scale_x) / (scale_x - 1)
    fixed_point_y = (y * scale_y) / (scale_y - 1)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.6f} {:.6f}".format(fixed_point_x, fixed_point_y))

if __name__ == "__main__":
    main()
