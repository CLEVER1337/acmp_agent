
import math

with open('INPUT.TXT', 'r') as f:
    S, R1 = map(float, f.readline().split())

S_circle = math.pi * R1 * R1
S_inner = S_circle - S
R2 = math.sqrt(S_inner / math.pi)

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{R2:.3f}")
