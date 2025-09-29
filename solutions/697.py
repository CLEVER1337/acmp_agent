
with open("INPUT.TXT", "r") as f:
    L, W, H = map(int, f.readline().split())

area = 2 * H * (L + W)
cans = area / 16
import math
result = math.ceil(cans)

with open("OUTPUT.TXT", "w") as f:
    f.write(str(result))
