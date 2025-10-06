
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
        
        send_events = {}
        recv_events = {}
        computer_queues = [deque() for _ in range(n)]
        message_computer = {}
        
        for comp_id, events in enumerate(protocols):
            for event in events:
                if event > 0:
                    msg_id = event
                    if msg_id not in send_events:
                        send_events[msg_id] = []
                    send_events[msg_id].append(comp_id)
                else:
                    msg_id = -event
                    if msg_id not in recv_events:
                        recv_events[msg_id] = []
                    recv_events[msg_id].append(comp_id)
        
        valid = True
        for msg_id in range(1, m+1):
            if msg_id not in send_events or msg_id not in recv_events:
                valid = False
                break
            if len(send_events[msg_id]) != 1 or len(recv_events[msg_id]) != 1:
                valid = False
                break
            sender = send_events[msg_id][0]
            receiver = recv_events[msg_id][0]
            message_computer[msg_id] = (sender, receiver)
        
        if not valid:
            output_lines.append("NO")
            continue
        
        in_degree = [0] * (m + 1)
        graph = [[] for _ in range(m + 1)]
        
        for comp_id, events in enumerate(protocols):
            current_msgs = []
            for event in events:
                if event > 0:
                    msg_id = event
                    current_msgs.append(msg_id)
                else:
                    msg_id = -event
                    if current_msgs and current_msgs[-1] == msg_id:
                        current_msgs.pop()
                    else:
                        valid = False
                        break
            if not valid:
                break
            
            stack = []
            for event in events:
                if event > 0:
                    msg_id = event
                    if stack:
                        prev_msg = stack[-1]
                        graph[prev_msg].append(msg_id)
                        in_degree[msg_id] += 1
                    stack.append(msg_id)
                else:
                    stack.pop()
        
        if not valid:
            output_lines.append("NO")
            continue
        
        queue = deque()
        for msg_id in range(1, m+1):
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
        
        if count == m:
            output_lines.append("YES")
        else:
            output_lines.append("NO")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
