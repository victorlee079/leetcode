from collections import defaultdict


def solution(debts):
    countries = defaultdict(int)
    for debt in debts:
        borrower, lender, amount = debt
        countries[borrower] -= amount
        countries[lender] += amount

    ans = []
    not_debt = True
    for k, v in sorted(countries.items(), key=lambda x:(x[1], x[0])):
        print(v)
        if v < 0:
            not_debt = False
        ans.append(k)
        
    if not not_debt:
        return ans
    else:
        return "No countries have debt."


print(solution([["USA", "Canada", 2], ["Canada", "USA", 2], ["Mexico", "USA", 5], ["Canada", "Mexico", 7],
                ["USA", "Canada", 4], ["USA", "Mexico", 4]]))

