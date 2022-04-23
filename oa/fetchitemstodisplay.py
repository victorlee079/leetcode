def solution(results, sort_column, sort_order, page_size, page_index):
    n = len(results)
    results = sorted(results, key=lambda x: x[sort_column], reverse=(sort_order == 1))
    start = page_size * page_index
    return [item[0] for item in results[start:start+page_size]]

print(solution([["foo.com", 10, 15], ["bar.com", 3, 4], ["baz.com", 17, 8]], 1, 0, 2, 1))
