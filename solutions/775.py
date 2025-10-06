
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    N_str = data[0]
    M_str = data[1]
    
    if M_str == '0':
        print("NO")
        return
        
    n = len(N_str)
    N = [int(d) for d in N_str]
    M = [int(d) for d in M_str]
    
    def add_one(num):
        num = num[:]
        carry = 1
        for i in range(len(num)-1, -1, -1):
            total = num[i] + carry
            num[i] = total % 10
            carry = total // 10
        if carry:
            num.insert(0, carry)
        return num
    
    def is_zero(num):
        return all(d == 0 for d in num)
    
    def compare(a, b):
        if len(a) > len(b):
            return 1
        if len(a) < len(b):
            return -1
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        return 0
    
    def subtract(a, b):
        a = a[:]
        b = b[:]
        while len(b) < len(a):
            b.insert(0, 0)
        result = []
        borrow = 0
        for i in range(len(a)-1, -1, -1):
            diff = a[i] - b[i] - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.insert(0, diff)
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return result
    
    def count_steps(x):
        steps = 0
        while not is_zero(x) and compare(x, [1]) != 0:
            steps += 1
            last_digit = x[-1]
            if last_digit % 2 == 0:
                carry = 0
                new_x = []
                for digit in x:
                    current = carry * 10 + digit
                    new_x.append(current // 2)
                    carry = current % 2
                while len(new_x) > 1 and new_x[0] == 0:
                    new_x.pop(0)
                x = new_x
            else:
                temp = [0] * len(x)
                carry = 0
                for i in range(len(x)-1, -1, -1):
                    total = x[i] * 3 + carry
                    temp[i] = total % 10
                    carry = total // 10
                if carry:
                    temp.insert(0, carry)
                x = add_one(temp)
        return steps
    
    current = add_one(N)
    end = add_one(N)
    carry = 0
    for i in range(len(M)-1, -1, -1):
        total = end[i] + M[i] + carry
        end[i] = total % 10
        carry = total // 10
    while carry:
        end.insert(0, carry % 10)
        carry //= 10
        
    min_steps = float('inf')
    best_k = None
    
    max_iterations = 1000
    iterations = 0
    
    while compare(current, end) <= 0 and iterations < max_iterations:
        iterations += 1
        steps = count_steps(current[:])
        if steps < min_steps:
            min_steps = steps
            best_k = current[:]
        
        current = add_one(current)
        if iterations >= max_iterations:
            break
            
    if best_k is not None:
        result_str = ''.join(str(d) for d in best_k)
        print(result_str)
    else:
        print("NO")

if __name__ == "__main__":
    main()
