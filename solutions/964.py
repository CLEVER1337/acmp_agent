
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    queries = data[1:1+n]
    
    # Структура данных: словарь {сайт: множество_ключевых_слов}
    sites = {}
    # Обратный индекс: словарь {ключевое_слово: множество_сайтов}
    inverted_index = {}
    
    output_lines = []
    
    for query in queries:
        parts = query.split()
        if parts[0] == 'Add':
            # Формат: Add keyword <keyword> to <site>
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in sites:
                sites[site] = set()
            
            if keyword in sites[site]:
                output_lines.append('Already exists')
            else:
                sites[site].add(keyword)
                # Обновляем обратный индекс
                if keyword not in inverted_index:
                    inverted_index[keyword] = set()
                inverted_index[keyword].add(site)
                output_lines.append('OK')
                
        elif parts[0] == 'Remove':
            # Формат: Remove keyword <keyword> from <site>
            keyword = parts[2]
            site = ' '.join(parts[4:])
            
            if site not in sites or keyword not in sites[site]:
                output_lines.append('Not found')
            else:
                sites[site].remove(keyword)
                # Обновляем обратный индекс
                if keyword in inverted_index and site in inverted_index[keyword]:
                    inverted_index[keyword].remove(site)
                    if len(inverted_index[keyword]) == 0:
                        del inverted_index[keyword]
                output_lines.append('OK')
                
        elif parts[0] == 'Search':
            # Формат: Search <keyword>
            keyword = ' '.join(parts[1:])
            
            if keyword not in inverted_index or len(inverted_index[keyword]) == 0:
                output_lines.append('Not found')
            else:
                # Получаем сайты и сортируем лексикографически
                found_sites = sorted(list(inverted_index[keyword]))
                # Берем первые 10
                result_sites = found_sites[:10]
                output_lines.append('\n'.join(result_sites))
    
    # Выводим результаты с разделителями
    result = '\n'.join(output_lines)
    print(result.replace('\n', '\n=====\n'))

if __name__ == "__main__":
    main()
