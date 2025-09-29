
def solve(nums):
    positive_sum = sum([i for i in nums if i > 0])
    
    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))
    
    product = 1
    start, end = (min_index, max_index) if min_index < max_index else (max_index, min_index)
    for i in range(start+1, end):
        product *= nums[i]
        
    return positive_sum, product

with open('INPUT.TXT', 'r') as file:
    n = int(file.readline())
    nums = list(map(int, file.readline().split()))
    
positive_sum, product = solve(nums)

with open('OUTPUT.TXT', 'w') as file:
    file.write(f'{positive_sum} {product}\n')
