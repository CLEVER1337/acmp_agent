
def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.read().splitlines()
    
    server_name = lines[0].split()[1]
    times = []
    
    for line in lines[1:5]:
        if line == 'Time out':
            continue
        if line.startswith('Reply from'):
            parts = line.split()
            time_str = parts[3].split('=')[1]
            times.append(int(time_str))
    
    lost_packets = 4 - len(times)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"Ping statistics for {server_name}:\n")
        f.write(f"    Packets: Sent = 4, Received = {len(times)}, Lost = {lost_packets} ({lost_packets * 25}% loss),\n")
        
        if times:
            min_time = min(times)
            max_time = max(times)
            avg_time = round(sum(times) / len(times))
            
            f.write("Approximate round trip times:\n")
            f.write(f"    Minimum = {min_time}ms, Maximum = {max_time}ms, Average = {avg_time}ms\n")

if __name__ == "__main__":
    main()
