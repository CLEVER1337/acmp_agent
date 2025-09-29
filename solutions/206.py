
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    idx = 0
    N = int(data[idx]); E = int(data[idx+1]); idx += 2
    M = int(data[idx]); idx += 1
    
    INF = 10**18
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    trains = []
    for _ in range(M):
        Ki = int(data[idx]); idx += 1
        stops = []
        for i in range(Ki):
            station = int(data[idx]); time = int(data[idx+1]); idx += 2
            stops.append((station, time))
        trains.append(stops)
    
    updated = True
    while updated:
        updated = False
        for stops in trains:
            min_time = INF
            for station, time in stops:
                if dist[station] <= time:
                    min_time = min(min_time, time)
            
            if min_time != INF:
                for station, time in stops:
                    if time >= min_time and dist[station] > time:
                        dist[station] = time
                        updated = True
    
    print(dist[E] if dist[E] != INF else -1)

if __name__ == "__main__":
    main()
