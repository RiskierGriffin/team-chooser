import random
players = []
file = open("players.txt", "r")
players = file.read().splitlines()
team_A = []
team_B = []

while (len(players) > 0):
    playerA = random.choice(players)
    team_A.append(playerA)
    players.remove(playerA)
    if players == []:
        break
    playerB = random.choice(players)
    team_B.append(playerB)
    players.remove(playerB)
print(team_A)
print(team_B)
