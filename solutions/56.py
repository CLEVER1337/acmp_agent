
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        friends = [f.readline().strip() for _ in range(n)]
        
        m = int(f.readline().strip())
        also_friends_of = [f.readline().strip() for _ in range(m)]
    
    friends_set = set(friends)
    also_friends_of_set = set(also_friends_of)
    
    mutual_friends = sorted(list(friends_set & also_friends_of_set))
    also_only = sorted(list(also_friends_of_set - friends_set))
    friends_sorted = sorted(friends)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"Friends: {', '.join(friends_sorted)}\n")
        f.write(f"Mutual Friends: {', '.join(mutual_friends)}\n")
        f.write(f"Also Friend of: {', '.join(also_only)}\n")

if __name__ == "__main__":
    main()
