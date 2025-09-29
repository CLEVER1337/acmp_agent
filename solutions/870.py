
import re

def is_valid_word(s):
    if not s:
        return False
    return all(c.isalnum() or c == '_' for c in s)

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def is_valid_domain(domain):
    if not domain:
        return False
    if len(domain) not in [2, 3]:
        return False
    return all(c.isalpha() for c in domain)

def is_valid_hostname(host):
    if is_valid_ip(host):
        return True
    
    parts = host.split('.')
    if len(parts) == 1:
        return is_valid_word(host)
    
    if len(parts) < 2:
        return False
    
    domain = parts[-1]
    if not is_valid_domain(domain):
        return False
    
    for part in parts[:-1]:
        if not is_valid_word(part):
            return False
    
    return True

def is_valid_port(port_str):
    if not port_str:
        return True
    if not port_str.isdigit():
        return False
    if len(port_str) > 1 and port_str[0] == '0':
        return False
    port = int(port_str)
    return 0 <= port <= 65535

def is_valid_path(path):
    if not path:
        return True
    parts = path.split('/')
    for part in parts:
        if not is_valid_word(part):
            return False
    return True

def is_valid_file(file_str):
    if not file_str:
        return True
    parts = file_str.split('.')
    for part in parts:
        if not is_valid_word(part):
            return False
    return True

def is_valid_url(line):
    line = line.strip()
    if not line:
        return False
    
    protocol = None
    host = None
    port = None
    path = None
    file = None
    
    protocol_match = re.match(r'^(http://)?([^:/?#\s]+)', line)
    if not protocol_match:
        return False
    
    protocol_part = protocol_match.group(1)
    rest = line[len(protocol_part or ''):]
    
    if protocol_part:
        protocol = protocol_part[:-3]
    
    port_match = re.search(r':(\d+)', rest)
    if port_match:
        port_start = port_match.start()
        host_part = rest[:port_start]
        port_part = port_match.group(1)
        rest = rest[port_match.end():]
    else:
        host_part = rest.split('/')[0]
        port_part = None
        rest = rest[len(host_part):]
    
    if not is_valid_hostname(host_part):
        return False
    
    if port_part and not is_valid_port(port_part):
        return False
    
    if rest:
        if rest[0] == '/':
            path_file_parts = rest[1:].split('/', 1)
            if len(path_file_parts) == 2:
                path_part, file_part = path_file_parts
            else:
                path_part = path_file_parts[0]
                file_part = None
            
            if path_part and not is_valid_path(path_part):
                return False
            
            if file_part and not is_valid_file(file_part):
                return False
        else:
            return False
    
    return True

def main():
    with open('INPUT.TXT', 'r') as f:
        lines = f.readlines()
    
    results = []
    for line in lines:
        if is_valid_url(line):
            results.append("YES")
        else:
            results.append("NO")
    
    with open('OUTPUT.TXT', 'w') as f:
        for result in results:
            f.write(result + '\n')

if __name__ == "__main__":
    main()
