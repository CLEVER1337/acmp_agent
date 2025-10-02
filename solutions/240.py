
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n = int(data[0].strip())
    views = []
    index = 1
    for _ in range(6):
        view = []
        for i in range(n):
            line = data[index].strip()
            index += 1
            view.append(line)
        views.append(view)
    
    front, left, back, right, top, bottom = views
    
    def get_view_color(view, i, j):
        return view[i][j]
    
    def is_possible(x, y, z):
        if get_view_color(front, z, x) == '.':
            return False
        if get_view_color(left, z, y) == '.':
            return False
        if get_view_color(back, z, n-1-x) == '.':
            return False
        if get_view_color(right, z, n-1-y) == '.':
            return False
        if get_view_color(top, n-1-z, x) == '.':
            return False
        if get_view_color(bottom, z, x) == '.':
            return False
            
        c1 = get_view_color(front, z, x)
        c2 = get_view_color(left, z, y)
        c3 = get_view_color(back, z, n-1-x)
        c4 = get_view_color(right, z, n-1-y)
        c5 = get_view_color(top, n-1-z, x)
        c6 = get_view_color(bottom, z, x)
        
        colors = [c1, c2, c3, c4, c5, c6]
        unique_colors = set(colors)
        return len(unique_colors) == 1
    
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if is_possible(x, y, z):
                    count += 1
                    
    print(count)

if __name__ == "__main__":
    main()
