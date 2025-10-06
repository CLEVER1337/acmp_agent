
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
    
    result = []
    current_pos = 0
    
    for i in range(n):
        app_id, window_id = windows[i]
        windows_in_app = app_windows[app_id]
        total_windows = len(windows_in_app)
        
        idx = windows_in_app.index(window_id)
        left_dist = idx
        right_dist = total_windows - idx
        
        app_cost = min(left_dist, right_dist)
        
        list_dist = min(abs(i - current_pos), n - abs(i - current_pos))
        
        total_cost = list_dist + app_cost
        result.append(str(total_cost))
        
        current_pos = i
    
    print(" ".join(result))

if __name__ == "__main__":
    main()
