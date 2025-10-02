
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    windows = []
    app_windows = {}
    
    for i in range(1, n + 1):
        parts = data[i].split()
        app_id = int(parts[0])
        window_id = int(parts[1])
        windows.append((app_id, window_id))
        
        if app_id not in app_windows:
            app_windows[app_id] = []
        app_windows[app_id].append(window_id)
    
    for app_id in app_windows:
        app_windows[app_id].sort()
    
    results = []
    current_pos = 0
    
    for i in range(n):
        app_id, window_id = windows[i]
        
        app_list = app_windows[app_id]
        m = len(app_list)
        
        pos_in_app = app_list.index(window_id)
        
        dist1 = abs(current_pos - i)
        dist2 = n - dist1
        dist_main = min(dist1, dist2)
        
        dist_app1 = pos_in_app
        dist_app2 = m - pos_in_app
        dist_app = min(dist_app1, dist_app2)
        
        total = dist_main + dist_app
        results.append(str(total))
        
        current_pos = i
    
    print(" ".join(results))

if __name__ == "__main__":
    main()
