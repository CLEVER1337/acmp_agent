
import re

def is_valid_word(s):
    if not s:
        return False
    return all(c.isalnum() or c == '_' for c in s)

def is_valid_ip(host):
    parts = host.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if part.startswith('0') and len(part) > 1:
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def is_valid_domain_name(host):
    if '.' in host:
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
    else:
        if not is_valid_word(host):
            return False
    return True

def is_valid_host(host):
    if is_valid_ip(host):
        return True
    return is_valid_domain_name(host)

def is_valid_port(port):
    if not port.isdigit():
        return False
    if port.startswith('0') and len(port) > 1:
        return False
    num = int(port)
    return 0 <= num <= 65535

def is_valid_path(path):
    if not path:
        return True
    parts = path.split('/')
    for part in parts:
        if not is_valid_word(part):
            return False
    return True

def is_valid_file(file):
    if not file:
        return True
    parts = file.split('.')
    for part in parts:
        if not is_valid_word(part):
            return False
    return True

def is_valid_url(line):
    line = line.strip()
    
    protocol_pattern = r'^(http://)?'
    host_pattern = r'([^:/]+)'
    port_pattern = r'(?::(\d+))?'
    path_pattern = r'(?:/([^/]*))?'
    file_pattern = r'(?:/([^/]*))?$'
    
    pattern = protocol_pattern + host_pattern + port_pattern + path_pattern + file_pattern
    match = re.match(pattern, line)
    
    if not match:
        return False
    
    protocol, host, port, path, file = match.groups()
    
    if protocol and protocol != 'http://':
        return False
    
    if not host:
        return False
    
    if not is_valid_host(host):
        return False
    
    if port and not is_valid_port(port):
        return False
    
    if path and not is_valid_path(path):
        return False
    
    if file and not is_valid_file(file):
        return False
    
    return True

with open('INPUT.TXT', 'r', encoding='utf-8') as f_in:
    with open('OUTPUT.TXT', 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if is_valid_url(line):
                f_out.write('YES\n')
            else:
                f_out.write('NO\n')
