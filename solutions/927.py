
MOD = 10**9 + 7

def main():
    c_str = input().strip()
    n = len(c_str)
    c_digits = [int(d) for d in c_str]
    
    dp = [[[[0] * 2 for _ in range(2)] for _ in range(10)] for _ in range(10)]
    
    for a_first in range(1, 10):
        for b_first in range(1, 10):
            total = a_first + b_first
            carry = total // 10
            digit = total % 10
            if digit != c_digits[-1]:
                continue
            a_prev = a_first
            b_prev = b_first
            valid = 1
            if a_first == b_first:
                valid = 0
            dp[a_first][b_first][carry][valid] = 1

    for pos in range(n-2, -1, -1):
        new_dp = [[[[0] * 2 for _ in range(2)] for _ in range(10)] for _ in range(10)]
        
        for a_prev in range(10):
            for b_prev in range(10):
                for carry_in in range(2):
                    for valid in range(2):
                        count = dp[a_prev][b_prev][carry_in][valid]
                        if count == 0:
                            continue
                            
                        for a_digit in range(10):
                            if a_digit == 0 and pos == 0:
                                continue
                            for b_digit in range(10):
                                if b_digit == 0 and pos == 0:
                                    continue
                                    
                                total = a_digit + b_digit + carry_in
                                carry_out = total // 10
                                digit = total % 10
                                
                                if digit != c_digits[pos]:
                                    continue
                                    
                                new_valid = valid
                                if a_digit == a_prev:
                                    new_valid = 0
                                if b_digit == b_prev:
                                    new_valid = 0
                                    
                                new_dp[a_digit][b_digit][carry_out][new_valid] = (
                                    new_dp[a_digit][b_digit][carry_out][new_valid] + count
                                ) % MOD
        
        dp = new_dp

    result = 0
    for a_digit in range(10):
        for b_digit in range(10):
            for carry_in in range(2):
                if carry_in != 0:
                    continue
                result = (result + dp[a_digit][b_digit][carry_in][1]) % MOD
    
    print(result)

if __name__ == "__main__":
    main()
