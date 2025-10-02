
def parse_time(s):
    parts = s.split(':')
    if len(parts) == 1:
        return 0, 0, int(parts[0])
    elif len(parts) == 2:
        return 0, int(parts[0]), int(parts[1])
    else:
        return int(parts[0]), int(parts[1]), int(parts[2])

def normalize(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    h = remaining_seconds // 3600
    remaining_seconds %= 3600
    m = remaining_seconds // 60
    s = remaining_seconds % 60
    return h, m, s, days

with open('INPUT.TXT', 'r') as f:
    current_time = f.readline().strip()
    interval = f.readline().strip()

h_cur, m_cur, s_cur = map(int, current_time.split(':'))
h_int, m_int, s_int = parse_time(interval)

total_seconds_current = h_cur * 3600 + m_cur * 60 + s_cur
total_seconds_interval = h_int * 3600 + m_int * 60 + s_int
total_seconds_result = total_seconds_current + total_seconds_interval

days = total_seconds_result // 86400
remaining_seconds = total_seconds_result % 86400

h_res = remaining_seconds // 3600
remaining_seconds %= 3600
m_res = remaining_seconds // 60
s_res = remaining_seconds % 60

with open('OUTPUT.TXT', 'w') as f:
    f.write(f"{h_res:02d}:{m_res:02d}:{s_res:02d}")
    if days > 0:
        f.write(f" +{days} days")
