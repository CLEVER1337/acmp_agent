
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    radii = list(map(int, data[1:1+n]))
    
    radii.sort(reverse=True)
    
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                r_i = radii[i]
                r_j = radii[j]
                r_k = radii[k]
                
                if r_i <= r_j or r_j <= r_k:
                    continue
                
                dist_ij = r_i + r_j
                dist_ik = r_i + r_k
                dist_jk = r_j + r_k
                
                angle_i = math.acos((dist_ij**2 + dist_ik**2 - dist_jk**2) / (2 * dist_ij * dist_ik))
                angle_j = math.acos((dist_ij**2 + dist_jk**2 - dist_ik**2) / (2 * dist_ij * dist_jk))
                angle_k = math.acos((dist_ik**2 + dist_jk**2 - dist_ij**2) / (2 * dist_ik * dist_jk))
                
                area_triangle = 0.5 * dist_ij * dist_ik * math.sin(angle_i)
                
                inradius = (2 * area_triangle) / (dist_ij + dist_ik + dist_jk)
                
                for l in range(k+1, n):
                    r_l = radii[l]
                    
                    if r_l >= inradius:
                        continue
                    
                    count += 1
    
    print(count)

if __name__ == "__main__":
    main()
