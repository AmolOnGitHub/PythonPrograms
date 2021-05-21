def getRanks(ranked):
    ranks = [1]
    i = 0
    rank = 1
    for score in ranked[1:]:
        if score == ranked[i]:
            ranks.append(rank)
        else:
            rank += 1
            ranks.append(rank)
        i += 1
    return ranks

n = int(input())
ranked = [int(x) for x in input().strip().split()]
m = int(input())
player = [int(x) for x in input().strip().split()]

temp = ranked

for score in player:
    temp.append(score)
    temp.sort(reverse = True)
    ranks = getRanks(temp)
    index = temp.index(score)
    print(ranks[index])