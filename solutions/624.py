
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
        
        # Build graph and check dependencies
        send_event = {}  # message_id -> (computer_id, event_index)
        recv_event = {}  # message_id -> (computer_id, event_index)
        
        # First pass: collect all events
        for comp_id, events in enumerate(protocols):
            for event_idx, event in enumerate(events):
                if event > 0:
                    if event in send_event:
                        # Multiple send events for same message - invalid
                        output_lines.append("NO")
                        break
                    send_event[event] = (comp_id, event_idx)
                else:
                    msg_id = -event
                    if msg_id in recv_event:
                        # Multiple receive events for same message - invalid
                        output_lines.append("NO")
                        break
                    recv_event[msg_id] = (comp_id, event_idx)
            else:
                continue
            break
        else:
            # Check if all messages have both send and receive events
            valid = True
            for msg_id in range(1, m+1):
                if msg_id not in send_event or msg_id not in recv_event:
                    valid = False
                    break
            
            if not valid:
                output_lines.append("NO")
                continue
            
            # Build dependency graph between events
            # We need to check that for each message, send happens before receive
            # and events on the same computer maintain their order
            
            # Create topological sort constraints
            # Each computer has its own event sequence constraints
            # Each message has send->receive constraint
            
            # We'll use a topological sort approach with Kahn's algorithm
            # Events are nodes, dependencies are edges
            
            total_nodes = total_events
            graph = [[] for _ in range(total_nodes)]
            in_degree = [0] * total_nodes
            
            # Map events to global indices
            global_index_map = {}
            global_idx = 0
            event_to_global = []
            
            for comp_id, events in enumerate(protocols):
                comp_events = []
                for event_idx in range(len(events)):
                    global_index_map[(comp_id, event_idx)] = global_idx
                    comp_events.append(global_idx)
                    global_idx += 1
                event_to_global.append(comp_events)
            
            # Add constraints from computer protocols (events must happen in order)
            for comp_id, events in enumerate(protocols):
                for event_idx in range(len(events) - 1):
                    u = event_to_global[comp_id][event_idx]
                    v = event_to_global[comp_id][event_idx + 1]
                    graph[u].append(v)
                    in_degree[v] += 1
            
            # Add constraints from messages (send must happen before receive)
            for msg_id in range(1, m+1):
                send_comp, send_idx = send_event[msg_id]
                recv_comp, recv_idx = recv_event[msg_id]
                
                u = event_to_global[send_comp][send_idx]
                v = event_to_global[recv_comp][recv_idx]
                
                graph[u].append(v)
                in_degree[v] += 1
            
            # Perform topological sort using Kahn's algorithm
            queue = deque()
            for i in range(total_nodes):
                if in_degree[i] == 0:
                    queue.append(i)
            
            count = 0
            while queue:
                u = queue.popleft()
                count += 1
                
                for v in graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            if count == total_nodes:
                output_lines.append("YES")
            else:
                output_lines.append("NO")
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
