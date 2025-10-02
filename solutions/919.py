
def main():
    with open('INPUT.TXT', 'r') as f:
        tw, th, w, h = map(int, f.read().split())
    
    def can_tile(tw, th, w, h):
        if (w % tw == 0 and h % th == 0) or (w % th == 0 and h % tw == 0):
            return True
        return False
    
    result = 'YES' if can_tile(tw, th, w, h) else 'NO'
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(result)

if __name__ == '__main__':
    main()
