import bisect


def solution(pricesOfJeans, pricesOfShoes, pricesOfSkirts, pricesOfTops, budget):
    pair_a = []
    for a in pricesOfJeans:
        for b in pricesOfShoes:
            if a + b < budget:
                pair_a.append(a + b)

    pair_b = []
    for a in pricesOfSkirts:
        for b in pricesOfTops:
            if a + b < budget:
                pair_b.append(a + b)

    if len(pair_a) > len(pair_b):
        pair_a, pair_b = pair_b, pair_a

    pair_b.sort()

    res = 0
    for i in pair_a:
        k = budget - i
        idx = bisect.bisect_right(pair_b, k)
        if idx != -1:
            res += idx
    return res