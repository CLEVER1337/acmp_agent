
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    circles = []
    index = 1
    for i in range(n):
        r = int(data[index])
        c = int(data[index+1])
        index += 2
        circles.append((r, c, i))
    
    centers = []
    for i in range(n):
        if i == 0:
            centers.append((0.0, 0.0))
        else:
            r_curr, c_curr, idx_curr = circles[i]
            best_x, best_y = 0.0, 0.0
            best_score = -10**18
            for j in range(i):
                r_j, c_j, idx_j = circles[j]
                x_j, y_j = centers[j]
                d = r_curr + r_j + 0.01
                angle_step = 2 * math.pi / 20
                for k in range(20):
                    angle = k * angle_step
                    x_candidate = x_j + d * math.cos(angle)
                    y_candidate = y_j + d * math.sin(angle)
                    if abs(x_candidate) > 10000 or abs(y_candidate) > 10000:
                        continue
                    valid = True
                    for l in range(i):
                        r_l, c_l, idx_l = circles[l]
                        x_l, y_l = centers[l]
                        dist = math.sqrt((x_candidate - x_l)**2 + (y_candidate - y_l)**2)
                        if dist < r_curr + r_l - 0.01:
                            valid = False
                            break
                    if not valid:
                        continue
                    score = 0
                    for l in range(i):
                        r_l, c_l, idx_l = circles[l]
                        x_l, y_l = centers[l]
                        dist = math.sqrt((x_candidate - x_l)**2 + (y_candidate - y_l)**2)
                        if dist < r_curr + r_l + 0.01 and dist > abs(r_curr - r_l) - 0.01:
                            score += c_l
                    if score > best_score:
                        best_score = score
                        best_x, best_y = x_candidate, y_candidate
            if best_score == -10**18:
                centers.append((0.0, 0.0))
            else:
                centers.append((best_x, best_y))
    
    for x, y in centers:
        print(f"{x:.10f} {y:.10f}")

if __name__ == "__main__":
    main()
