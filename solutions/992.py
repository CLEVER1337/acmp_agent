
import sys

def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    m = list(map(int, data[1:1+k]))
    
    if k == 0:
        print("0")
        return
        
    result = []
    n = sum(m)
    
    if n == 0:
        print("1")
        print("0")
        return
        
    if k == 1:
        if m[0] % 2 == 0:
            print("1")
            print("0")
        else:
            print("1")
            print("1 1")
        return
        
    rows = []
    for i in range(k):
        rows.append((m[i], i))
        
    def get_irreducible_diagrams():
        diagrams = set()
        diagrams.add(tuple(m))
        
        queue = [tuple(m)]
        visited = set()
        visited.add(tuple(m))
        
        while queue:
            current = queue.pop(0)
            current_list = list(current)
            len_current = len(current_list)
            
            for i in range(len_current):
                if i < len_current - 1 and current_list[i] > current_list[i + 1]:
                    if current_list[i] >= 2 and current_list[i + 1] >= 1:
                        new_list = current_list[:]
                        new_list[i] -= 2
                        new_list[i + 1] -= 1
                        while new_list and new_list[-1] == 0:
                            new_list.pop()
                        new_tuple = tuple(new_list)
                        if new_tuple not in visited:
                            visited.add(new_tuple)
                            queue.append(new_tuple)
                            diagrams.add(new_tuple)
                            
                if i > 0 and current_list[i - 1] > current_list[i]:
                    if current_list[i] >= 2:
                        new_list = current_list[:]
                        new_list[i] -= 2
                        while new_list and new_list[-1] == 0:
                            new_list.pop()
                        new_tuple = tuple(new_list)
                        if new_tuple not in visited:
                            visited.add(new_tuple)
                            queue.append(new_tuple)
                            diagrams.add(new_tuple)
                            
            for i in range(len_current):
                if current_list[i] >= 2:
                    new_list = current_list[:]
                    new_list[i] -= 2
                    while new_list and new_list[-1] == 0:
                        new_list.pop()
                    new_tuple = tuple(new_list)
                    if new_tuple not in visited:
                        visited.add(new_tuple)
                        queue.append(new_tuple)
                        diagrams.add(new_tuple)
                        
        irreducible = set()
        for diagram in diagrams:
            is_irreducible = True
            diagram_list = list(diagram)
            len_diagram = len(diagram_list)
            
            for i in range(len_diagram):
                if i < len_diagram - 1 and diagram_list[i] > diagram_list[i + 1]:
                    if diagram_list[i] >= 2 and diagram_list[i + 1] >= 1:
                        is_irreducible = False
                        break
                if i > 0 and diagram_list[i - 1] > diagram_list[i]:
                    if diagram_list[i] >= 2:
                        is_irreducible = False
                        break
                if diagram_list[i] >= 2:
                    is_irreducible = False
                    break
                    
            if is_irreducible:
                irreducible.add(diagram)
                
        return list(irreducible)
        
    irreducible_diagrams = get_irreducible_diagrams()
    
    print(len(irreducible_diagrams))
    for diagram in irreducible_diagrams:
        if len(diagram) == 0:
            print("0")
        else:
            print(f"{len(diagram)} {' '.join(map(str, diagram))}")
            
if __name__ == "__main__":
    main()
