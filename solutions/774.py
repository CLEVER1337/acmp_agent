
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    m = int(data[1])
    R = float(data[2])
    H = float(data[3])
    a_list = list(map(float, data[4:4+n]))
    cities = []
    index = 4 + n
    for i in range(m):
        city_prices = list(map(int, data[index:index+n]))
        cities.append(city_prices)
        index += n
    
    max_profit = 0
    
    for city_idx in range(m):
        for jewel_type in range(n):
            a = a_list[jewel_type]
            price = cities[city_idx][jewel_type]
            
            if a > 2 * R:
                continue
                
            max_per_layer = min(5, int(math.floor(2 * R / a)))
            
            layers = int(math.floor(H / a))
            
            total_containers = max_per_layer * layers
            
            profit = total_containers * price
            
            if profit > max_profit:
                max_profit = profit
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(max_profit))

if __name__ == "__main__":
    main()
