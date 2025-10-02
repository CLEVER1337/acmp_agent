
def ip_to_bin(ip):
    parts = list(map(int, ip.split('.')))
    return ''.join(f'{part:08b}' for part in parts)

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    n = int(data[0])
    masks = []
    for i in range(1, n+1):
        mask = data[i].strip()
        masks.append(ip_to_bin(mask))
    
    m = int(data[n+1])
    results = []
    
    for i in range(n+2, n+2+m):
        ip1, ip2 = data[i].strip().split()
        bin_ip1 = ip_to_bin(ip1)
        bin_ip2 = ip_to_bin(ip2)
        
        count = 0
        for mask in masks:
            masked_ip1 = ''.join('1' if m_bit == '1' and ip1_bit == '1' else '0' 
                               for m_bit, ip1_bit in zip(mask, bin_ip1))
            masked_ip2 = ''.join('1' if m_bit == '1' and ip2_bit == '1' else '0' 
                               for m_bit, ip2_bit in zip(mask, bin_ip2))
            
            if masked_ip1 == masked_ip2:
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
