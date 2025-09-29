
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    windows = []
    app_windows = {}
    
    for i in range(1, n + 1):
        app_id, window_pos = map(int, data[i].split())
        windows.append((app_id, window_pos))
        
        if app_id not in app_windows:
            app_windows[app_id] = []
        app_windows[app_id].append(window_pos)
    
    for app_id in app_windows:
        app_windows[app_id].sort()
    
    result = []
    current_pos = 0
    
    for i in range(n):
        app_id, window_pos = windows[i]
        app_list = app_windows[app_id]
        m = len(app_list)
        
        idx = app_list.index(window_pos)
        
        dist_in_app = min(idx, m - idx)
        
        dist_in_global = min(abs(i - current_pos), n - abs(i - current_pos))
        
        total = dist_in_global + dist_in_app
        result.append(str(total))
        
        current_pos = i
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
