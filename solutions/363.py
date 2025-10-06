
def main():
    with open('INPUT.TXT', 'r') as f:
        M = f.readline().strip()
        N = f.readline().strip()
    
    if M == '0' or N == '0':
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    sign = 1
    if M[0] == '-':
        sign *= -1
        M = M[1:]
    if N[0] == '-':
        sign *= -1
        N = N[1:]
    
    lenM = len(M)
    lenN = len(N)
    result = [0] * (lenM + lenN)
    
    for i in range(lenM-1, -1, -1):
        carry = 0
        n1 = int(M[i])
        for j in range(lenN-1, -1, -1):
            n2 = int(N[j])
            temp = n1 * n2 + result[i+j+1] + carry
            carry = temp // 10
            result[i+j+1] = temp % 10
        result[i] += carry
    
    start_index = 0
    while start_index < len(result) and result[start_index] == 0:
        start_index += 1
    
    if start_index == len(result):
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    output = ''.join(str(x) for x in result[start_index:])
    if sign == -1:
        output = '-' + output
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()
