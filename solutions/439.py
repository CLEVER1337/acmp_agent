
def main():
    with open('INPUT.TXT', 'r') as f:
        n, p = map(int, f.read().split())
    
    parallel_part = (100 - p) / 100
    sequential_part = p / 100
    
    if parallel_part == 0:
        speedup = 1.0
    else:
        total_time = sequential_part + parallel_part / n
        speedup = 1.0 / total_time
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.6f}".format(speedup))

if __name__ == "__main__":
    main()
