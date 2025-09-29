
def main():
    with open("INPUT.TXT", "r") as f:
        k1, l1, m1 = map(int, f.readline().split())
        k2, l2, m2 = map(int, f.readline().split())
    
    bolts_left = k1 * (100 - l1) // 100
    nuts_left = k2 * (100 - l2) // 100
    
    pairs = min(bolts_left, nuts_left)
    
    bolts_damage = (k1 - bolts_left) * m1 + (bolts_left - pairs) * m1
    nuts_damage = (k2 - nuts_left) * m2 + (nuts_left - pairs) * m2
    
    total_damage = bolts_damage + nuts_damage
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(total_damage))

if __name__ == "__main__":
    main()
