
def next_permutation(s):
    arr = list(s)
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return None
        
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    
    arr[i:] = arr[len(arr)-1:i-1:-1]
    return ''.join(arr)

with open('INPUT.TXT', 'r') as f:
    word = f.readline().strip()

result = next_permutation(word)

with open('OUTPUT.TXT', 'w') as f:
    f.write(result)
