
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    
    if K < 0:
        print(0)
        return
        
    def count_numbers_with_k_zeros(n, k):
        from math import comb
        
        def count_up_to(x, k):
            s = bin(x)[2:]
            n_bits = len(s)
            total = 0
            
            for length in range(1, n_bits):
                if length - 1 >= k:
                    total += comb(length - 1, k)
            
            ones_so_far = 0
            for i, bit in enumerate(s):
                remaining_bits = n_bits - i - 1
                if bit == '1':
                    if remaining_bits > 0:
                        needed_zeros = k - ones_so_far
                        if needed_zeros >= 0 and needed_zeros <= remaining_bits:
                            total += comb(remaining_bits, needed_zeros)
                    ones_so_far += 1
                else:
                    if ones_so_far > k:
                        break
            if bin(x).count('0') == k:
                total += 1
            return total
        
        return count_up_to(n, k)
    
    result = count_numbers_with_k_zeros(N, K)
    print(result)

if __name__ == "__main__":
    main()
