
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    people = []
    index = 1
    for i in range(n):
        t = int(data[index])
        w = int(data[index + 1])
        index += 2
        people.append((t, w, i))
    
    people.sort(key=lambda x: x[1], reverse=True)
    
    result = [0] * n
    stack = []
    
    for i in range(n):
        t, w, idx = people[i]
        if not stack:
            stack.append((t, w, idx))
            result[idx] = t * w
        else:
            last_t, last_w, last_idx = stack[-1]
            if t < last_t:
                stack.append((t, w, idx))
                result[idx] = t * w
            else:
                total_time = result[last_idx]
                while stack and t >= stack[-1][0]:
                    prev_t, prev_w, prev_idx = stack.pop()
                    total_time = result[prev_idx]
                stack.append((t, w, idx))
                result[idx] = total_time
    
    for i in range(n):
        print(result[i])

if __name__ == "__main__":
    main()
