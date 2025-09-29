
def ip_to_bin(ip):
    parts = list(map(int, ip.split('.')))
    return ''.join(f'{part:08b}' for part in parts)

def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    n = int(data[0])
    masks = []
    for i in range(1, 1 + n):
        masks.append(data[i])
    
    m = int(data[1 + n])
    pairs = []
    for i in range(2 + n, 2 + n + m):
        pairs.append(data[i].split())
    
    bin_masks = []
    for mask in masks:
        bin_mask = ip_to_bin(mask)
        bin_masks.append(bin_mask)
    
    results = []
    for pair in pairs:
        ip1, ip2 = pair
        bin_ip1 = ip_to_bin(ip1)
        bin_ip2 = ip_to_bin(ip2)
        
        count = 0
        for bin_mask in bin_masks:
            masked_ip1 = ''.join('1' if bm == '1' and bi == '1' else '0' for bm, bi in zip(bin_mask, bin_ip1))
            masked_ip2 = ''.join('1' if bm == '1' and bi == '1' else '0' for bm, bi in zip(bin_mask, bin_ip2))
            
            if masked_ip1 == masked_ip2:
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
