
with open('INPUT.TXT', 'r') as f:
    n = int(f.readline().strip())
    max_age = -1
    result_index = -1
    
    for i in range(1, n + 1):
        data = f.readline().split()
        age = int(data[0])
        gender = int(data[1])
        
        if gender == 1:
            if age > max_age:
                max_age = age
                result_index = i
            elif age == max_age and result_index == -1:
                result_index = i

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(result_index))
