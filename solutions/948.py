
with open('INPUT.TXT', 'r') as f:
    K, N = map(int, f.readline().split())

page = (N - 1) // K + 1
line_on_page = (N - 1) % K + 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{page} {line_on_page}")
