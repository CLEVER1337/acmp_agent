
import sys

def read_input():
    data = sys.stdin.read().splitlines()
    tests = []
    current = []
    for line in data:
        if line.strip() == '':
            if current:
                tests.append(current)
                current = []
        else:
            current.append(line)
    if current:
        tests.append(current)
    return tests

def parse_test(test):
    n, k = map(int, test[0].split())
    sets = []
    for i in range(1, k+1):
        s = list(map(int, test[i].split()))
        sets.append(s)
    return n, k, sets

def find_next_partition(n, k, sets):
    elements = [0] * (n+1)
    part_id = [0] * (n+1)
    for idx, s in enumerate(sets):
        for num in s:
            elements[num] = 1
            part_id[num] = idx

    max_num = n
    while max_num > 0 and elements[max_num] == 1:
        max_num -= 1
    if max_num == 0:
        return generate_first(n)

    current_part = part_id[max_num]
    can_merge = False
    target_num = max_num
    for num in range(max_num+1, n+1):
        if elements[num] == 1 and part_id[num] < current_part:
            can_merge = True
            target_num = num
            break

    if can_merge:
        new_sets = []
        for i in range(len(sets)):
            s = sets[i]
            if i == part_id[target_num]:
                new_set = [x for x in s if x != target_num]
                new_set.append(max_num)
                new_set.sort()
                new_sets.append(new_set)
            elif i == current_part:
                new_set = [x for x in s if x != max_num]
                new_set.append(target_num)
                new_set.sort()
                new_sets.append(new_set)
            else:
                new_sets.append(s)
        new_sets.sort(key=lambda x: (len(x), x))
        return new_sets
    else:
        new_sets = []
        merged = False
        for i in range(len(sets)):
            s = sets[i]
            if i == current_part:
                new_set = [x for x in s if x != max_num]
                new_sets.append(new_set)
                new_set = [max_num]
                new_sets.append(new_set)
                merged = True
            else:
                new_sets.append(s)
        if not merged:
            new_sets.append([max_num])
        new_sets = [s for s in new_sets if s]
        new_sets.sort(key=lambda x: (len(x), x))
        return new_sets

def generate_first(n):
    return [[i] for i in range(1, n+1)]

def main():
    tests = read_input()
    output_lines = []
    for test in tests:
        if test[0] == '0 0':
            continue
        n, k, sets = parse_test(test)
        next_partition = find_next_partition(n, k, sets)
        output_lines.append(f"{n} {len(next_partition)}")
        for s in next_partition:
            output_lines.append(" ".join(map(str, s)))
        output_lines.append("")
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
