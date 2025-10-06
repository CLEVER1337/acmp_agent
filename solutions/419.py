
def main():
    s = input().strip()
    filtered = []
    for char in s:
        if 'a' <= char <= 'z':
            filtered.append(char)
        elif 'A' <= char <= 'Z':
            filtered.append(char.lower())
    
    n = len(filtered)
    if n == 0:
        print("YES")
        print("a")
        return
        
    def is_palindrome(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
        
    if is_palindrome(filtered):
        print("YES")
        print(''.join(filtered))
        return
        
    left, right = 0, n - 1
    mismatch_left = -1
    mismatch_right = -1
    while left < right:
        if filtered[left] != filtered[right]:
            mismatch_left = left
            mismatch_right = right
            break
        left += 1
        right -= 1
        
    if mismatch_left != -1:
        candidate1 = filtered[:mismatch_left] + filtered[mismatch_left+1:]
        candidate2 = filtered[:mismatch_right] + filtered[mismatch_right+1:]
        candidate3 = filtered[:mismatch_right] + [filtered[mismatch_left]] + filtered[mismatch_right:]
        candidate4 = filtered[:mismatch_left+1] + [filtered[mismatch_right]] + filtered[mismatch_left+1:]
        
        if is_palindrome(candidate1) or is_palindrome(candidate2) or is_palindrome(candidate3) or is_palindrome(candidate4):
            pal = None
            if is_palindrome(candidate1):
                pal = candidate1
            elif is_palindrome(candidate2):
                pal = candidate2
            elif is_palindrome(candidate3):
                pal = candidate3
            else:
                pal = candidate4
            print("YES")
            print(''.join(pal))
            return
            
        print("NO")
    else:
        print("YES")
        print(''.join(filtered))

if __name__ == "__main__":
    main()
