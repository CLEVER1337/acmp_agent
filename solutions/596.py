
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    stations = []
    index = 1
    for _ in range(n):
        operator = data[index].strip()
        index += 1
        x, y, r = map(int, data[index].split())
        index += 1
        stations.append((operator, x, y, r))
    
    xa, ya = map(int, data[index].split())
    
    operators_order = []
    operator_counts = {}
    operator_stations_count = {}
    
    for operator, x, y, r in stations:
        if operator not in operator_stations_count:
            operator_stations_count[operator] = 0
            operators_order.append(operator)
        
        distance_sq = (x - xa)**2 + (y - ya)**2
        if distance_sq <= r*r:
            operator_counts[operator] = operator_counts.get(operator, 0) + 1
    
    k = len(operators_order)
    result = [str(k)]
    
    for operator in operators_order:
        count = operator_counts.get(operator, 0)
        result.append(f"{operator} {count}")
    
    print("\n".join(result))

if __name__ == "__main__":
    main()
