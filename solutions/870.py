
import sys
import re

def is_valid_word(s):
    if not s:
        return False
    for c in s:
        if not (c.isalnum() or c == '_'):
            return False
    return True

def is_valid_ip(host):
    parts = host.split('.')
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

def is_valid_hostname(host):
    if '.' not in host:
        return is_valid_word(host)
    
    parts = host.split('.')
    if len(parts) < 2:
        return False
    
    domain = parts[-1]
    if not (len(domain) == 2 or len(domain) == 3):
        return False
    if not domain.isalpha():
        return False
    
    for part in parts[:-1]:
        if not is_valid_word(part):
            return False
    
    return True

def is_valid_port(port_str):
    if not port_str.isdigit():
        return False
    if len(port_str) > 1 and port_str[0] == '0':
        return False
    port = int(port_str)
    return 0 <= port <= 65535

def is_valid_path(path):
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
    file_part = None
    
    protocol_match = re.match(r'^(http://)?(.+)$', line)
    if not protocol_match:
        return False
    
    protocol_part = protocol_match.group(1)
    rest = protocol_match.group(2)
    
    if protocol_part and protocol_part != 'http://':
        return False
    
    host_port_match = re.match(r'^([^:/]+)(?::(\d+))?(?:(/.*))?$', rest)
    if not host_port_match:
        return False
    
    host = host_port_match.group(1)
    port_str = host_port_match.group(2)
    path_file = host_port_match.group(3)
    
    if port_str:
        if not is_valid_port(port_str):
            return False
        port = port_str
    
    if not host:
        return False
    
    if not (is_valid_ip(host) or is_valid_hostname(host)):
        return False
    
    if path_file:
        path_file_parts = path_file.split('/', 1)
        first_part = path_file_parts[0]
        
        if len(path_file_parts) == 1:
            if '.' in first_part:
                file_part = first_part
                if not is_valid_file(file_part):
                    return False
            else:
                path = first_part
                if not is_valid_path(path):
                    return False
        else:
            path_part = path_file_parts[0]
            remaining = path_file_parts[1]
            
            if path_part:
                if not is_valid_path(path_part):
                    return False
                path = path_part
            
            if '.' in remaining:
                last_slash = remaining.rfind('/')
                if last_slash != -1:
                    path_remaining = remaining[:last_slash]
                    file_remaining = remaining[last_slash + 1:]
                    
                    if path_remaining:
                        full_path = (path + '/' + path_remaining if path else path_remaining)
                        if not is_valid_path(full_path):
                            return False
                    
                    if file_remaining:
                        if not is_valid_file(file_remaining):
                            return False
                else:
                    if not is_valid_file(remaining):
                        return False
            else:
                full_path = (path + '/' + remaining if path else remaining)
                if not is_valid_path(full_path):
                    return False
    
    return True

def main():
    data = sys.stdin.read().splitlines()
    results = []
    
    for line in data:
        if is_valid_url(line):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
