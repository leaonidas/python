import json


def gTop(goals):
    pointsGame = 0
    if goals >= 1.5:
        pointsGame = 2.7
    elif goals < 1.5 and goals >= 1:
        pointsGame = 2.3
    elif goals < 1 and goals >= 0.5:
        pointsGame = 2
    elif goals < 0.5 and goals >= 0:
        pointsGame = 1.5
    elif goals < 0 and goals >= -0.5:
        pointsGame = 0.7
    elif goals < -0.5 and goals >= -1:
        pointsGame = 0.5
    elif goals < -1 and goals >= -1.5:
        pointsGame = 0.3
    elif goals < -1.5:
        pointsGame = 0.1

    return pointsGame


with open('table.json') as f:
    table = json.load(f)

with open('xg.json') as f:
    xgmatch = json.load(f)

for team in table:
    name = team['team']
    xgTotal = 0
    exPoints = 0
    xG = 0
    xGA = 0
    for match in xgmatch:
        if match['home_team'] == name:
            exPoints += gTop(match['home_xG'] - match['away_xG'])
            xG += match['home_xG']
            xGA += match['away_xG']
        elif match['away_team'] == name:
            exPoints += gTop(match['away_xG'] - match['home_xG'])
            xGA += match['home_xG']
            xG += match['away_xG']
    print(name + '\nExpected points: ' + str(exPoints) + ' Real points: ' +
          str(team['points']) + '\nExpected Goals: ' + str(xG) + ' Real goals: ' + str(team['goalsFor']) + '\nExpected goals against: ' + str(xGA) + ' Real goals against: ' + str(team['goalsAgainst']) + '\n')
