
def main():
    s = input().strip()
    n = len(s)
    
    if n == 0:
        print("NO SOLUTION")
        return
        
    # Проверяем, все ли символы одинаковые
    if all(c == s[0] for c in s):
        print("NO SOLUTION")
        return
        
    # Проверяем, является ли вся строка палиндромом
    is_palindrome = True
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            is_palindrome = False
            break
            
    if not is_palindrome:
        print(s)
        return
        
    # Ищем наибольшую подстроку, не являющуюся палиндромом
    # Это будет либо вся строка без первого символа, либо вся строка без последнего
    # Проверяем обе варианта и выбираем наибольшую
    candidate1 = s[:-1]  # без последнего символа
    candidate2 = s[1:]   # без первого символа
    
    if len(candidate1) > len(candidate2):
        print(candidate1)
    else:
        print(candidate2)

if __name__ == "__main__":
    main()
