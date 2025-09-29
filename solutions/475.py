
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        nums = list(map(int, data))
    
    n = len(nums)
    if n < 2:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('No')
        return
    
    nums.sort()
    diff = nums[1] - nums[0]
    
    for i in range(2, n):
        if nums[i] - nums[i-1] != diff:
            with open('OUTPUT.TXT', 'w') as f:
                f.write('No')
            return
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write('Yes')

if __name__ == '__main__':
    main()
