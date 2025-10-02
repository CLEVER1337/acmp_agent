
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
    
    for t, w, idx in people:
        current_time = t * w
        while stack:
            prev_t, prev_w, prev_idx, prev_total = stack[-1]
            if prev_t * prev_w >= current_time:
                break
            stack.pop()
            current_time = max(current_time, prev_total + t * (w - prev_w))
        stack.append((t, w, idx, current_time))
        result[idx] = current_time
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
