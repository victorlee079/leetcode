class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        mem = [0] * len(transactions)
        d = defaultdict(list)
        for i in range(len(transactions)):
            trans = transactions[i]
            name, time, amount, city = trans.split(",")
            
            if int(amount) > 1000:
                mem[i] = 1

            history = d[name]
            for ptime, pcity, pi in history:
                if (int(ptime) + 60 >= int(time) >= int(ptime) - 60) and pcity != city:
                    mem[pi] = 1
                    mem[i] = 1
            d[name].append((time, city, i))
            
        res = []
        for i in range(len(transactions)):
            if mem[i] == 1:
                res.append(transactions[i])
        return res
