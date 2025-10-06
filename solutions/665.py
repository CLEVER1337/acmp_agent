
s = input().strip()
h, m = map(int, s.split(':'))
total_minutes = h * 60 + m

for i in range(total_minutes + 1, total_minutes + 24 * 60):
    time = i % (24 * 60)
    hours = time // 60
    minutes = time % 60
    time_str = f"{hours:02d}:{minutes:02d}"
    if time_str == time_str[::-1]:
        print(time_str)
        break
