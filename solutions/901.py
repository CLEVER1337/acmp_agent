
def main():
    with open("INPUT.TXT", "r") as f:
        N = int(f.read().strip())
    
    def lcm(a, b):
        from math import gcd
        return a * b // gcd(a, b)
    
    def max_cycle_length(n):
        cycles = []
        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                cycle_length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle_length += 1
                    j = (j * 2) % n if (j * 2) % n != 0 else n
                cycles.append(cycle_length)
        
        result = 1
        for cycle in cycles:
            result = lcm(result, cycle)
        return result
    
    result = max_cycle_length(N) - 1
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
