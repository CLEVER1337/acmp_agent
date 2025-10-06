
def main():
    n = int(input().strip())
    records = [input().strip() for _ in range(n)]
    subjects = set()
    
    for record in records:
        found = False
        for subject in subjects:
            if record.startswith(subject) or subject.startswith(record):
                if len(record) > len(subject):
                    subjects.remove(subject)
                    subjects.add(record)
                found = True
                break
        if not found:
            subjects.add(record)
            
    print(len(subjects))

if __name__ == "__main__":
    main()
