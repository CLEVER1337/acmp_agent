
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    queries = data[1:1+n]
    
    sites = {}
    keyword_to_sites = {}
    
    output_lines = []
    
    for query in queries:
        if query.startswith('Add keyword'):
            parts = query.split()
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in sites:
                sites[site] = set()
            
            if keyword in sites[site]:
                output_lines.append('Already exists')
            else:
                sites[site].add(keyword)
                
                if keyword not in keyword_to_sites:
                    keyword_to_sites[keyword] = set()
                keyword_to_sites[keyword].add(site)
                output_lines.append('OK')
                
        elif query.startswith('Remove keyword'):
            parts = query.split()
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in sites or keyword not in sites[site]:
                output_lines.append('Not found')
            else:
                sites[site].remove(keyword)
                
                if keyword in keyword_to_sites and site in keyword_to_sites[keyword]:
                    keyword_to_sites[keyword].remove(site)
                    if len(keyword_to_sites[keyword]) == 0:
                        del keyword_to_sites[keyword]
                output_lines.append('OK')
                
        elif query.startswith('Search'):
            keyword = query.split()[1]
            
            if keyword not in keyword_to_sites or len(keyword_to_sites[keyword]) == 0:
                output_lines.append('Not found')
            else:
                sorted_sites = sorted(keyword_to_sites[keyword])
                result = ', '.join(sorted_sites[:10])
                output_lines.append(result)
    
    print('\n'.join(output_lines))

if __name__ == "__main__":
    main()
