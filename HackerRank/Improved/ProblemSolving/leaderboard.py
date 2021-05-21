n = int(input().strip())
ranked = list(set([int(scores_temp) for scores_temp in input().strip().split(' ')]))
# Converting to set and back to list removes the duplicates in a list
ranked.sort(reverse = True)

m = int(input().strip())
player = [int(alice_temp) for alice_temp in input().strip().split(' ')]

for score in player:
    while len(ranked) > 0 and ranked[-1] <= score:
        del ranked[-1]
    
    print(len(ranked) + 1)