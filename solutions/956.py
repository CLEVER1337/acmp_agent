
def main():
    note_list = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note_aliases = {
        'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#',
        'A#': 'Bb', 'D#': 'Eb', 'G#': 'Ab', 'C#': 'Db'
    }
    
    n = int(input().strip())
    open_notes = input().split()
    chord_name = input().strip()
    
    for i in range(len(open_notes)):
        if open_notes[i] in note_aliases:
            open_notes[i] = note_aliases[open_notes[i]]
    
    tonic = chord_name[0]
    if len(chord_name) > 1 and chord_name[1] in ['#', 'b']:
        tonic += chord_name[1]
        chord_type = chord_name[2:]
    else:
        chord_type = chord_name[1:]
    
    if tonic in note_aliases:
        tonic = note_aliases[tonic]
    
    tonic_index = note_list.index(tonic)
    
    if chord_type == '':
        intervals = [0, 4, 7]
    elif chord_type == 'm':
        intervals = [0, 3, 7]
    elif chord_type == '7':
        intervals = [0, 4, 7, 10]
    elif chord_type == 'm7':
        intervals = [0, 3, 7, 10]
    else:
        intervals = [0]
    
    chord_notes = set()
    for interval in intervals:
        note_index = (tonic_index + interval) % 12
        chord_notes.add(note_list[note_index])
    
    count = 0
    max_fret = n
    
    def generate_combinations(current, index):
        nonlocal count
        if index == 6:
            played_notes = set()
            for i in range(6):
                fret = current[i]
                open_note = open_notes[i]
                open_index = note_list.index(open_note)
                note_index = (open_index + fret) % 12
                played_notes.add(note_list[note_index])
            
            if played_notes == chord_notes:
                count += 1
            return
        
        for fret in range(0, max_fret + 1):
            generate_combinations(current + [fret], index + 1)
    
    generate_combinations([], 0)
    print(count)

if __name__ == "__main__":
    main()
