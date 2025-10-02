
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n_ternary, m_ternary = data[0], data[1]
    
    def ternary_to_decimal(ternary_str):
        decimal = 0
        for i, digit in enumerate(reversed(ternary_str)):
            decimal += int(digit) * (3 ** i)
        return decimal
    
    n_decimal = ternary_to_decimal(n_ternary)
    m_decimal = ternary_to_decimal(m_ternary)
    result = n_decimal + m_decimal
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
