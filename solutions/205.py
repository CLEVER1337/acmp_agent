
def parse_time(s):
    parts = list(map(int, s.split(':')))
    if len(parts) == 1:
        return 0, 0, parts[0]
    elif len(parts) == 2:
        return 0, parts[0], parts[1]
    else:
        return parts[0], parts[1], parts[2]

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def from_seconds(total_seconds):
    days = total_seconds // 86400
    remaining = total_seconds % 86400
    h = remaining // 3600
    remaining %= 3600
    m = remaining // 60
    s = remaining % 60
    return h, m, s, days

def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

with open("INPUT.TXT", "r") as f:
    current_time = f.readline().strip()
    interval = f.readline().strip()

h_cur, m_cur, s_cur = map(int, current_time.split(':'))
h_int, m_int, s_int = parse_time(interval)

total_current = to_seconds(h_cur, m_cur, s_cur)
total_interval = to_seconds(h_int, m_int, s_int)
total_result = total_current + total_interval

h_res, m_res, s_res, days = from_seconds(total_result)

result = format_time(h_res, m_res, s_res)
if days > 0:
    result += f" +{days} days"

with open("OUTPUT.TXT", "w") as f:
    f.write(result)
