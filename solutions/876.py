
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        A, B, R = map(float, f.readline().split())
    
    # Нормализуем вектор (A, B) для получения направления максимума
    length = math.sqrt(A*A + B*B)
    if length > 0:
        x0 = (A / length) * R
        y0 = (B / length) * R
    else:
        x0 = R
        y0 = 0
    
    max_value = A * x0 + B * y0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{max_value:.10f}\n")
        f.write(f"{x0:.10f} {y0:.10f}\n")

if __name__ == "__main__":
    main()
