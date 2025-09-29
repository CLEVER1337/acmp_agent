
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    results = []
    
    for i in range(1, n + 1):
        word = data[i].strip()
        count0 = 0
        count1 = 0
        count2 = 0
        valid = True
        
        for char in word:
            if char == '0':
                if count1 > 0 or count2 > 0:
                    valid = False
                    break
                count0 += 1
            elif char == '1':
                if count2 > 0:
                    valid = False
                    break
                count1 += 1
            elif char == '2':
                count2 += 1
            else:
                valid = False
                break
                
        if valid and count0 == count1 == count2 and count0 > 0:
            results.append("YES")
        else:
            results.append("NO")
            
    with open('OUTPUT.TXT', 'w') as f:
        for result in results:
            f.write(result + '\n')

if __name__ == "__main__":
    main()
