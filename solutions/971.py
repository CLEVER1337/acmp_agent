
def main():
    with open("INPUT.TXT", "r") as f:
        x, y = map(int, f.readline().split())
    
    # Простейшее решение: одна вершина в (3x, 3y), остальные в (0, 0)
    # Проверяем, что координаты центра масс можно представить в виде (a+b+c)/3
    
    # Всегда существует решение - берем вершины:
    # A(3x, 3y), B(0, 0), C(0, 0)
    # Центр масс: ((3x+0+0)/3, (3y+0+0)/3) = (x, y)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write("YES\n")
        f.write(f"{3*x} {3*y}\n")
        f.write("0 0\n")
        f.write("0 0\n")

if __name__ == "__main__":
    main()
