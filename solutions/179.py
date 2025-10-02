
def main():
    with open('INPUT.TXT', 'r') as f:
        k = int(f.read().strip())
    
    if k == 0:
        result = 2
    else:
        a, b = 1, 1
        total = a + b
        
        for _ in range(k):
            new_numbers = []
            for i in range(len(sequence) - 1):
                new_sum = sequence[i] + sequence[i + 1]
                new_numbers.append(new_sum)
                total += new_sum
            
            new_sequence = []
            for i in range(len(sequence)):
                new_sequence.append(sequence[i])
                if i < len(sequence) - 1:
                    new_sequence.append(new_numbers[i])
            sequence = new_sequence
        
        result = total
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
