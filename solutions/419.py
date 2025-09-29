
import sys

def is_letter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def normalize(s):
    return ''.join(c.lower() for c in s if is_letter(c))

def is_palindrome(s):
    return s == s[::-1]

def find_palindrome(s):
    normalized = normalize(s)
    n = len(normalized)
    
    if is_palindrome(normalized):
        return s
    
    for i in range(len(normalized)):
        # Попробовать удалить символ
        candidate = normalized[:i] + normalized[i+1:]
        if is_palindrome(candidate):
            return reconstruct_original(s, candidate, i, 'delete')
        
        # Попробовать заменить символ
        for j in range(i + 1, len(normalized)):
            if normalized[i] != normalized[j]:
                candidate = list(normalized)
                candidate[i] = candidate[j]
                candidate = ''.join(candidate)
                if is_palindrome(candidate):
                    return reconstruct_original(s, candidate, i, 'replace')
    
    # Попробовать добавить символ
    for i in range(len(normalized) + 1):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            candidate = normalized[:i] + char + normalized[i:]
            if is_palindrome(candidate):
                return reconstruct_original(s, candidate, i, 'add', char)
    
    return None

def reconstruct_original(original, palindrome, pos, operation, added_char=None):
    letters_only = [c for c in original if is_letter(c)]
    non_letters = [c for c in original if not is_letter(c)]
    
    if operation == 'delete':
        # Восстановить оригинал, вставив удаленный символ обратно
        result = []
        letter_idx = 0
        for c in original:
            if is_letter(c):
                if letter_idx == pos:
                    result.append(c)
                result.append(c)
                letter_idx += 1
            else:
                result.append(c)
        return ''.join(result)
    
    elif operation == 'replace':
        # Восстановить оригинал, заменив символ обратно
        result = []
        letter_idx = 0
        for c in original:
            if is_letter(c):
                if letter_idx == pos:
                    result.append(c)
                else:
                    result.append(c)
                letter_idx += 1
            else:
                result.append(c)
        return ''.join(result)
    
    elif operation == 'add':
        # Восстановить оригинал, удалив добавленный символ
        result = []
        letter_idx = 0
        for c in original:
            if is_letter(c):
                result.append(c)
                letter_idx += 1
            else:
                result.append(c)
        return ''.join(result)

def main():
    data = sys.stdin.read().strip()
    if not data:
        print("NO")
        return
    
    normalized = normalize(data)
    
    # Проверить, является ли строка палиндромом
    if is_palindrome(normalized):
        print("YES")
        print(data)
        return
    
    # Проверить возможность исправления одним изменением
    result = find_palindrome(data)
    
    if result:
        print("YES")
        print(result)
    else:
        print("NO")

if __name__ == "__main__":
    main()
