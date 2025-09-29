
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

year = int(input())
if is_leap(year):
    day = 256 - 244
    print(f"{day:02d}/09/{year:04d}")
else:
    day = 256 - 243
    print(f"{day:02d}/09/{year:04d}")
