
def main():
    with open("INPUT.TXT", "r") as f:
        data = f.read().split()
    
    if len(data) < 2:
        with open("OUTPUT.TXT", "w") as f:
            f.write("NO")
        return
    
    word1 = data[0]
    word2 = data[1]
    
    if len(word1) != len(word2):
        with open("OUTPUT.TXT", "w") as f:
            f.write("NO")
        return
    
    count1 = {}
    count2 = {}
    
    for char in word1:
        count1[char] = count1.get(char, 0) + 1
        
    for char in word2:
        count2[char] = count2.get(char, 0) + 1
        
    if count1 == count2:
        with open("OUTPUT.TXT", "w") as f:
            f.write("YES")
    else:
        with open("OUTPUT.TXT", "w") as f:
            f.write("NO")

if __name__ == "__main__":
    main()
