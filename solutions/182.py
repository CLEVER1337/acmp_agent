
with open('INPUT.TXT', 'r') as f:
    data = list(map(int, f.readline().split()))

points = [(data[i], data[i+1]) for i in range(0, 6, 2)]

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

x4 = sum(set(x_coords)) * 2 - sum(x_coords)
y4 = sum(set(y_coords)) * 2 - sum(y_coords)

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{x4} {y4}")
