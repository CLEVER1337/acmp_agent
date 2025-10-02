
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    auth = int(data[1])
    friends = []
    index = 2
    for i in range(n):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        friends.append((a, b, i+1))
        
    # Разделяем друзей на тех, у кого bi >= 0 и bi < 0
    positive = []
    negative = []
    for a, b, idx in friends:
        if b >= 0:
            positive.append((a, b, idx))
        else:
            negative.append((a, b, idx))
            
    # Сортируем положительных по ai (по возрастанию)
    positive.sort(key=lambda x: x[0])
    
    # Сортируем отрицательных по ai + bi (по убыванию), что эквивалентно (a + b)
    negative.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    selected = []
    current_auth = auth
    
    # Обрабатываем сначала положительных друзей
    for a, b, idx in positive:
        if current_auth >= a:
            current_auth += b
            selected.append(idx)
    
    # Обрабатываем отрицательных друзей
    for a, b, idx in negative:
        if current_auth >= a:
            current_auth += b
            selected.append(idx)
        else:
            break
    
    print(len(selected))
    if selected:
        print(" ".join(map(str, selected)))

if __name__ == "__main__":
    main()
