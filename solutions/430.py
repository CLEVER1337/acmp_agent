
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        R = float(f.readline().strip())
        lat1, lon1 = map(float, f.readline().split())
        lat2, lon2 = map(float, f.readline().split())
    
    phi1 = math.radians(90 - lat1)
    phi2 = math.radians(90 - lat2)
    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)
    
    cos_psi = math.sin(phi1) * math.sin(phi2) * math.cos(lambda1 - lambda2) + math.cos(phi1) * math.cos(phi2)
    cos_psi = max(-1.0, min(1.0, cos_psi))
    
    psi = math.acos(cos_psi)
    distance = R * psi
    
    print("{:.2f}".format(distance))

if __name__ == "__main__":
    main()
