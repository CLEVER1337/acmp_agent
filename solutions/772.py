
def main():
    import sys
    data = sys.stdin.readline().split()
    n = int(data[0])
    m = int(data[1])
    bends = data[2:2+m]
    
    layers = []
    for i in range(n + 1):
        layers.append((i, 'F'))
    
    for bend in bends:
        point = int(bend[:-1])
        direction = bend[-1]
        
        left = layers[:point]
        right = layers[point:]
        
        if direction == 'F':
            right = [(idx, 'R' if side == 'F' else 'F') for idx, side in reversed(right)]
            layers = left + right
        else:
            left = [(idx, 'R' if side == 'F' else 'F') for idx, side in reversed(left)]
            layers = left + right
            
        if len(layers) != len(set(idx for idx, _ in layers)):
            print("SCRUFFY")
            return
            
    result_F = []
    result_R = []
    for idx, side in layers:
        if side == 'F':
            result_F.append(f"P{idx}F")
        else:
            result_R.append(f"P{idx}R")
            
    output = " ".join(result_F + result_R)
    print(output)

if __name__ == "__main__":
    main()
