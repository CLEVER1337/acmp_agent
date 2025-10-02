
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
    
    if n == 0:
        return "a"
    
    if is_palindrome(normalized):
        return s
    
    for i in range(n // 2 + 1):
        j = n - 1 - i
        if normalized[i] != normalized[j]:
            # Попробуем удалить символ слева
            if is_palindrome(normalized[i+1:j+1]):
                return reconstruct_with_deletion(s, i)
            
            # Попробуем удалить символ справа
            if is_palindrome(normalized[i:j]):
                return reconstruct_with_deletion(s, j)
            
            # Попробуем заменить символ
            if i != j:
                return reconstruct_with_replacement(s, i, j, normalized[j])
            
            # Попробуем добавить символ
            return reconstruct_with_addition(s, i, normalized[i])
    
    return s

def reconstruct_with_deletion(s, pos):
    letters = [c for c in s if is_letter(c)]
    result = []
    letter_count = 0
    
    for c in s:
        if is_letter(c):
            if letter_count != pos:
                result.append(c)
            letter_count += 1
        else:
            result.append(c)
    
    return ''.join(result)

def reconstruct_with_replacement(s, left_pos, right_pos, correct_char):
    letters = [c for c in s if is_letter(c)]
    result = []
    letter_count = 0
    
    for c in s:
        if is_letter(c):
            if letter_count == left_pos:
                result.append(correct_char.upper() if c.isupper() else correct_char)
            else:
                result.append(c)
            letter_count += 1
        else:
            result.append(c)
    
    return ''.join(result)

def reconstruct_with_addition(s, pos, correct_char):
    letters = [c for c in s if is_letter(c)]
    result = []
    letter_count = 0
    
    for c in s:
        if is_letter(c):
            if letter_count == pos:
                result.append(correct_char.upper() if c.isupper() else correct_char)
                result.append(c)
            else:
                result.append(c)
            letter_count += 1
        else:
            result.append(c)
    
    return ''.join(result)

def main():
    with open('INPUT.TXT', 'r', encoding='utf-8') as f:
        s = f.readline().strip()
    
    normalized = normalize(s)
    
    if is_palindrome(normalized):
        with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
            f.write("YES\n")
            f.write(s + "\n")
        return
    
    n = len(normalized)
    found = False
    
    for i in range(n // 2 + 1):
        j = n - 1 - i
        if normalized[i] != normalized[j]:
            # Проверяем возможность удаления одного символа
            if is_palindrome(normalized[i+1:j+1]) or is_palindrome(normalized[i:j]):
                found = True
                break
            
            # Проверяем возможность замены одного символа
            if i != j and (normalized[:i] + normalized[j] + normalized[i+1:]) == (normalized[:i] + normalized[j] + normalized[i+1:])[::-1]:
                found = True
                break
            
            # Проверяем возможность добавления одного символа
            test_str = normalized[:i] + normalized[j] + normalized[i:]
            if is_palindrome(test_str):
                found = True
                break
            
            test_str = normalized[:j+1] + normalized[i] + normalized[j+1:]
            if is_palindrome(test_str):
                found = True
                break
    
    if found:
        palindrome = find_palindrome(s)
        with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
            f.write("YES\n")
            f.write(palindrome + "\n")
    else:
        with open('OUTPUT.TXT', 'w', encoding='utf-8') as f:
            f.write("NO\n")

if __name__ == "__main__":
    main()
