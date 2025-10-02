
def main():
    note_order = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note_aliases = {
        'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#',
        'A#': 'Bb', 'D#': 'Eb', 'G#': 'Ab', 'C#': 'Db'
    }
    
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    N = int(lines[0].strip())
    open_strings = lines[1].strip().split()
    chord_name = lines[2].strip()
    
    for i in range(len(open_strings)):
        if open_strings[i] in note_aliases:
            open_strings[i] = note_aliases[open_strings[i]]
    
    tonic = chord_name
    chord_type = ''
    if 'maj7' in chord_name:
        tonic = chord_name[:-4]
        chord_type = 'maj7'
    elif 'min7' in chord_name:
        tonic = chord_name[:-4]
        chord_type = 'min7'
    elif 'm' in chord_name:
        tonic = chord_name[:-1]
        chord_type = 'm'
    else:
        chord_type = ''
    
    if tonic in note_aliases:
        tonic = note_aliases[tonic]
    
    tonic_idx = note_order.index(tonic)
    
    if chord_type == '':
        chord_notes = [
            note_order[tonic_idx],
            note_order[(tonic_idx + 4) % 12],
            note_order[(tonic_idx + 7) % 12]
        ]
    elif chord_type == 'm':
        chord_notes = [
            note_order[tonic_idx],
            note_order[(tonic_idx + 3) % 12],
            note_order[(tonic_idx + 7) % 12]
        ]
    elif chord_type == 'maj7':
        chord_notes = [
            note_order[tonic_idx],
            note_order[(tonic_idx + 4) % 12],
            note_order[(tonic_idx + 7) % 12],
            note_order[(tonic_idx + 11) % 12]
        ]
    elif chord_type == 'min7':
        chord_notes = [
            note_order[tonic_idx],
            note_order[(tonic_idx + 3) % 12],
            note_order[(tonic_idx + 7) % 12],
            note_order[(tonic_idx + 10) % 12]
        ]
    
    chord_notes_set = set(chord_notes)
    
    count = 0
    for s1 in range(N + 1):
        note1 = note_order[(note_order.index(open_strings[0]) + s1) % 12]
        if note1 not in chord_notes_set:
            continue
        for s2 in range(N + 1):
            note2 = note_order[(note_order.index(open_strings[1]) + s2) % 12]
            if note2 not in chord_notes_set:
                continue
            for s3 in range(N + 1):
                note3 = note_order[(note_order.index(open_strings[2]) + s3) % 12]
                if note3 not in chord_notes_set:
                    continue
                for s4 in range(N + 1):
                    note4 = note_order[(note_order.index(open_strings[3]) + s4) % 12]
                    if note4 not in chord_notes_set:
                        continue
                    for s5 in range(N + 1):
                        note5 = note_order[(note_order.index(open_strings[4]) + s5) % 12]
                        if note5 not in chord_notes_set:
                            continue
                        for s6 in range(N + 1):
                            note6 = note_order[(note_order.index(open_strings[5]) + s6) % 12]
                            if note6 not in chord_notes_set:
                                continue
                            
                            played_notes = {note1, note2, note3, note4, note5, note6}
                            if played_notes == chord_notes_set:
                                count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
