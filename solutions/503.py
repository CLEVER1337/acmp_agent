
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    planets = []
    for i in range(1, n+1):
        parts = data[i].split()
        t = parts[0]
        c1 = int(parts[1])
        p1 = int(parts[2])
        c2 = int(parts[3])
        p2 = int(parts[4])
        planets.append((t, c1, p1, c2, p2))
    
    total_mask = (1 << n) - 1
    INF = 10**9
    dp = [[INF] * n for _ in range(1 << n)]
    prev = [[-1] * n for _ in range(1 << n)]
    
    for i in range(n):
        mask = 1 << i
        t, c1, p1, c2, p2 = planets[i]
        cost = 0
        if t == 'C':
            cost += p1
        else:
            cost += c1
        dp[mask][i] = cost
        prev[mask][i] = -1
    
    for mask in range(1, 1 << n):
        for last in range(n):
            if dp[mask][last] == INF:
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                new_mask = mask | (1 << nxt)
                t_curr, c1_curr, p1_curr, c2_curr, p2_curr = planets[last]
                t_nxt, c1_nxt, p1_nxt, c2_nxt, p2_nxt = planets[nxt]
                
                cost_add = 0
                if t_nxt == 'C':
                    cost_add += p1_nxt
                else:
                    cost_add += c1_nxt
                
                if t_curr == 'C':
                    cost_add += p2_curr
                else:
                    cost_add += c2_curr
                
                new_cost = dp[mask][last] + cost_add
                if new_cost < dp[new_mask][nxt]:
                    dp[new_mask][nxt] = new_cost
                    prev[new_mask][nxt] = last
                elif new_cost == dp[new_mask][nxt]:
                    if prev[new_mask][nxt] == -1:
                        prev[new_mask][nxt] = last
                    else:
                        path1 = []
                        cur_mask = new_mask
                        cur_last = nxt
                        while cur_last != -1:
                            path1.append(cur_last)
                            old_mask = cur_mask
                            cur_mask ^= (1 << cur_last)
                            cur_last = prev[old_mask][cur_last]
                        path1.reverse()
                        
                        path2 = []
                        cur_mask = new_mask
                        cur_last = nxt
                        temp_prev = last
                        while temp_prev != -1:
                            path2.append(cur_last)
                            cur_last = temp_prev
                            cur_mask ^= (1 << nxt)
                            temp_prev = prev[cur_mask][cur_last]
                        path2.append(cur_last)
                        path2.reverse()
                        
                        for idx in range(len(path1)):
                            if path1[idx] != path2[idx]:
                                if path2[idx] < path1[idx]:
                                    prev[new_mask][nxt] = last
                                break
    
    best_cost = INF
    best_last = -1
    for last in range(n):
        if dp[total_mask][last] < best_cost:
            best_cost = dp[total_mask][last]
            best_last = last
        elif dp[total_mask][last] == best_cost:
            if best_last == -1:
                best_last = last
            else:
                path1 = []
                cur_mask = total_mask
                cur_last = last
                while cur_last != -1:
                    path1.append(cur_last)
                    old_mask = cur_mask
                    cur_mask ^= (1 << cur_last)
                    cur_last = prev[old_mask][cur_last]
                path1.reverse()
                
                path2 = []
                cur_mask = total_mask
                cur_last = best_last
                while cur_last != -1:
                    path2.append(cur_last)
                    old_mask = cur_mask
                    cur_mask ^= (1 << cur_last)
                    cur_last = prev[old_mask][cur_last]
                path2.reverse()
                
                for idx in range(len(path1)):
                    if path1[idx] != path2[idx]:
                        if path1[idx] < path2[idx]:
                            best_last = last
                        break
    
    path = []
    cur_mask = total_mask
    cur_last = best_last
    while cur_last != -1:
        path.append(cur_last)
        old_mask = cur_mask
        cur_mask ^= (1 << cur_last)
        cur_last = prev[old_mask][cur_last]
    path.reverse()
    
    total_cost = best_cost
    for i in range(n):
        if planets[i][0] == 'C':
            total_cost += planets[i][4]
        else:
            total_cost += planets[i][3]
    
    print(total_cost)
    print("0", end="")
    for p in path:
        print(f" {p+1}", end="")
    print(" 0")

if __name__ == "__main__":
    main()
