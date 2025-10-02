
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        records = [line.strip() for line in f.readlines()]
    
    subjects = set()
    
    for record in records:
        found = False
        for subject in list(subjects):
            if record.startswith(subject) or subject.startswith(record):
                if len(record) > len(subject):
                    subjects.remove(subject)
                    subjects.add(record)
                found = True
                break
        if not found:
            subjects.add(record)
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(len(subjects)))

if __name__ == "__main__":
    main()
