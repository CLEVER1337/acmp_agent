
def main():
    note_list = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note_aliases = {
        'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#',
        'A#': 'Bb', 'D#': 'Eb', 'G#': 'Ab', 'C#': 'Db'
    }
    
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        tuning = f.readline().split()
        chord_name = f.readline().strip()
    
    for i in range(len(tuning)):
        if tuning[i] in note_aliases:
            tuning[i] = note_aliases[tuning[i]]
    
    tonic = chord_name[0]
    if len(chord_name) > 1 and chord_name[1] in ['#', 'b']:
        tonic += chord_name[1]
        chord_type = chord_name[2:]
    else:
        chord_type = chord_name[1:]
    
    if tonic in note_aliases:
        tonic = note_aliases[tonic]
    
    chord_notes = set()
    base_index = note_list.index(tonic)
    
    if chord_type == '':
        chord_notes.add(note_list[base_index])
        chord_notes.add(note_list[(base_index + 4) % 12])
        chord_notes.add(note_list[(base_index + 7) % 12])
    elif chord_type == 'm':
        chord_notes.add(note_list[base_index])
        chord_notes.add(note_list[(base_index + 3) % 12])
        chord_notes.add(note_list[(base_index + 7) % 12])
    elif chord_type == '7':
        chord_notes.add(note_list[base_index])
        chord_notes.add(note_list[(base_index + 4) % 12])
        chord_notes.add(note_list[(base_index + 7) % 12])
        chord_notes.add(note_list[(base_index + 10) % 12])
    elif chord_type == 'm7':
        chord_notes.add(note_list[base_index])
        chord_notes.add(note_list[(base_index + 3) % 12])
        chord_notes.add(note_list[(base_index + 7) % 12])
        chord_notes.add(note_list[(base_index + 10) % 12])
    
    count = 0
    for fret1 in range(n + 1):
        note1 = note_list[(note_list.index(tuning[0]) + fret1) % 12]
        if note1 not in chord_notes:
            continue
        for fret2 in range(n + 1):
            note2 = note_list[(note_list.index(tuning[1]) + fret2) % 12]
            if note2 not in chord_notes:
                continue
            for fret3 in range(n + 1):
                note3 = note_list[(note_list.index(tuning[2]) + fret3) % 12]
                if note3 not in chord_notes:
                    continue
                for fret4 in range(n + 1):
                    note4 = note_list[(note_list.index(tuning[3]) + fret4) % 12]
                    if note4 not in chord_notes:
                        continue
                    for fret5 in range(n + 1):
                        note5 = note_list[(note_list.index(tuning[4]) + fret5) % 12]
                        if note5 not in chord_notes:
                            continue
                        for fret6 in range(n + 1):
                            note6 = note_list[(note_list.index(tuning[5]) + fret6) % 12]
                            if note6 not in chord_notes:
                                continue
                            
                            played_notes = {note1, note2, note3, note4, note5, note6}
                            if played_notes.issubset(chord_notes) and len(played_notes) == len(chord_notes):
                                count += 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(count))

if __name__ == '__main__':
    main()
