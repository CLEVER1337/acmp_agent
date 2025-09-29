
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        songs = []
        song_dict = {}
        for i in range(n):
            data = f.readline().split()
            name = data[0]
            duration = int(data[1])
            songs.append((name, duration))
            song_dict[name] = {'duration': duration, 'rating': 0, 'index': i}
        
        m, k = map(int, f.readline().split())
        played_songs = []
        for _ in range(m):
            played_songs.append(f.readline().strip())
        
        switch_times = list(map(int, f.readline().split()))
    
    current_time = 0
    switch_index = 0
    
    for i in range(m):
        song_name = played_songs[i]
        duration = song_dict[song_name]['duration']
        
        if switch_index < k and current_time + duration > switch_times[switch_index]:
            song_dict[song_name]['rating'] -= 1
            current_time = switch_times[switch_index]
            switch_index += 1
        else:
            song_dict[song_name]['rating'] += 1
            current_time += duration
    
    result = []
    for name, duration in songs:
        result.append(str(song_dict[name]['rating']))
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(result))

if __name__ == '__main__':
    main()
