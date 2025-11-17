
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    day = int(data[0])
    month = int(data[1])

    # Days per month in leap year 2008 (February has 29 days)
    days_in_month = [0,
        31, 29, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]   # index 1..12

    # win[day][month] – True if player to move from this date can force a win
    # we use extra index 0 for simplicity, and allocate up to day 31
    win = [[False] * 13 for _ in range(32)]

    # Compute DP in reverse chronological order
    for m in range(12, 0, -1):
        max_day = days_in_month[m]
        for d in range(max_day, 0, -1):
            # (31,12) is a losing move – we never consider it as a safe target
            if d == 31 and m == 12:
                continue

            winning = False

            # increase day by 1
            nd = d + 1
            if nd <= max_day and not (nd == 31 and m == 12):
                if not win[nd][m]:
                    winning = True

            # increase day by 2
            if not winning:
                nd = d + 2
                if nd <= max_day and not (nd == 31 and m == 12):
                    if not win[nd][m]:
                        winning = True

            # increase month by 1
            if not winning:
                nm = m + 1
                if nm <= 12 and d <= days_in_month[nm] and not (d == 31 and nm == 12):
                    if not win[d][nm]:
                        winning = True

            # increase month by 2
            if not winning:
                nm = m + 2
                if nm <= 12 and d <= days_in_month[nm] and not (d == 31 and nm == 12):
                    if not win[d][nm]:
                        winning = True

            win[d][m] = winning

    result = 1 if win[day][month] else 2
    sys.stdout.write(str(result))

if __name__ == "__main__":
    solve()
