from random import choices
ntrials = 10000
player1wins = 0
for i in range(ntrials):
    total1 = 0
    total2 = 0
    dice1 = choices(range(1, 7), k=2)
    total1 = total1 + dice1[0] + dice1[1]
    if dice1[0] == dice1[1]:
        player1wins += 1
        continue
    dice2 = choices(range(1, 7), k=3)
    dice2.sort(reverse=True)
    total2 = total2 + dice2[0] + dice2[1]
    if total2 <= total1:
        player1wins +=1
print("player1wins=", player1wins/ntrials)