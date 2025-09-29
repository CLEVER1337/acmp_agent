
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); index += 2
        protocols = []
        total_events = 0
        
        for i in range(n):
            k = int(data[index]); index += 1
            events = list(map(int, data[index:index+k]))
            index += k
            protocols.append(events)
            total_events += k
        
        message_to_computer = {}
        send_events = [[] for _ in range(n)]
        receive_events = [[] for _ in range(n)]
        
        for comp_id, events in enumerate(protocols):
            for event in events:
                msg_id = abs(event)
                if event > 0:
                    send_events[comp_id].append(msg_id)
                    if msg_id in message_to_computer:
                        output_lines.append("NO")
                        break
                    message_to_computer[msg_id] = comp_id
                else:
                    receive_events[comp_id].append(msg_id)
        
        if output_lines and output_lines[-1] == "NO":
            continue
            
        in_degree = [0] * (m + 1)
        graph = [[] for _ in range(m + 1)]
        msg_ids = set()
        
        for comp_id in range(n):
            send_queue = deque(send_events[comp_id])
            receive_queue = deque(receive_events[comp_id])
            
            while send_queue and receive_queue:
                s_msg = send_queue[0]
                r_msg = receive_queue[0]
                
                if s_msg == r_msg:
                    send_queue.popleft()
                    receive_queue.popleft()
                else:
                    graph[s_msg].append(r_msg)
                    in_degree[r_msg] += 1
                    send_queue.popleft()
                    msg_ids.add(s_msg)
                    msg_ids.add(r_msg)
            
            if send_queue or receive_queue:
                output_lines.append("NO")
                break
        else:
            queue = deque()
            for msg_id in msg_ids:
                if in_degree[msg_id] == 0:
                    queue.append(msg_id)
            
            count = 0
            while queue:
                u = queue.popleft()
                count += 1
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            if count == len(msg_ids):
                output_lines.append("YES")
            else:
                output_lines.append("NO")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
