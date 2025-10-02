
import math

def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    R = float(data[2])
    H = float(data[3])
    
    a_list = list(map(float, data[4:4+n]))
    
    cities = []
    index = 4 + n
    for i in range(m):
        row = list(map(int, data[index:index+n]))
        cities.append(row)
        index += n
    
    max_profit = 0
    
    for city_idx in range(m):
        for jewel_type in range(n):
            a = a_list[jewel_type]
            
            if a > 2 * R:
                continue
                
            max_in_layer = 0
            for count in range(1, 6):
                angle = 2 * math.asin(a / (2 * R))
                if count * angle <= 2 * math.pi + 1e-9:
                    max_in_layer = count
            
            if max_in_layer == 0:
                continue
                
            layers = int(H // a)
            total_count = layers * max_in_layer
            profit = total_count * cities[city_idx][jewel_type]
            
            if profit > max_profit:
                max_profit = profit
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(max_profit))

if __name__ == "__main__":
    main()
