
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    queries = data[1:1+n]
    
    site_keywords = {}
    keyword_sites = {}
    
    output_lines = []
    
    for query in queries:
        parts = query.split()
        if parts[0] == 'Add':
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in site_keywords:
                site_keywords[site] = set()
            
            if keyword in site_keywords[site]:
                output_lines.append("Already exists")
            else:
                site_keywords[site].add(keyword)
                
                if keyword not in keyword_sites:
                    keyword_sites[keyword] = set()
                keyword_sites[keyword].add(site)
                output_lines.append("OK")
                
        elif parts[0] == 'Remove':
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in site_keywords or keyword not in site_keywords[site]:
                output_lines.append("Not found")
            else:
                site_keywords[site].remove(keyword)
                keyword_sites[keyword].remove(site)
                if not keyword_sites[keyword]:
                    del keyword_sites[keyword]
                output_lines.append("OK")
                
        elif parts[0] == 'Search':
            keyword = parts[1]
            
            if keyword not in keyword_sites or not keyword_sites[keyword]:
                output_lines.append("Not found")
            else:
                sites_list = sorted(keyword_sites[keyword])
                result = ', '.join(sites_list[:10])
                output_lines.append(result)
    
    print('\n'.join(output_lines))
    print('=' * 5)

if __name__ == "__main__":
    main()
