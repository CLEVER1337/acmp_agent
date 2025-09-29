
a, b, c = map(int, input().split())
surface_area = 2 * (a * b + a * c + b * c)
volume = a * b * c
print(surface_area, volume)
