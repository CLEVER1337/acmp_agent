
with open('INPUT.TXT', 'r') as f:
    data = list(map(int, f.readline().split()))

total_days = 31
weekends_per_employee = 4

total_work_days = sum(data)
employees = total_work_days // (total_days - weekends_per_employee)

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(employees))
