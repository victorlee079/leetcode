class Solution:
  # O(n+100001)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            losses_count = [-1] * 100001

            for winner, loser in matches:
                if losses_count[winner] == -1:
                    losses_count[winner] = 0
                if losses_count[loser] == -1:
                    losses_count[loser] = 1
                else:
                    losses_count[loser] += 1
                
            answer = [[], []]
            for i in range(100001):
                if losses_count[i] == 0:
                    answer[0].append(i)
                elif losses_count[i] == 1:
                    answer[1].append(i)
                    
            return answer
          
    # O(n log n)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        winners = defaultdict(int)
        losers = defaultdict(int)

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            winners[winner] += 1
            losers[loser] += 1
        players = sorted(list(players))

        ret, win, lose = [], [], []

        for player in players:
            if player in winners and player not in losers:
                win.append(player)
            if player in losers and losers[player] == 1:
                lose.append(player)

        ret.append(win)
        ret.append(lose)
        return ret
