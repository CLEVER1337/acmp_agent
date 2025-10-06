
import math

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    R = float(data[2])
    H = float(data[3])
    a_list = list(map(float, data[4:4+n]))
    index = 4 + n
    cities = []
    for i in range(m):
        row = list(map(int, data[index:index+n]))
        index += n
        cities.append(row)
    
    max_profit = 0
    for city_idx in range(m):
        for jewel_type in range(n):
            a = a_list[jewel_type]
            if a > 2 * R:
                count = 0
            else:
                d = 2 * R
                max_per_layer = int(d / a)
                max_per_layer = min(max_per_layer, 5)
                
                if max_per_layer == 0:
                    count = 0
                else:
                    layers = int(H / a)
                    count = layers * max_per_layer
            
            profit = count * cities[city_idx][jewel_type]
            if profit > max_profit:
                max_profit = profit
                
    print(max_profit)

if __name__ == "__main__":
    main()
