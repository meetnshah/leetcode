# We're asked to imagine there is an algorithms tournament taking place in which multiple teams compete against each other.
# In each competition there will be two teams that compete and there will be one winner and one loser out of all of these competitions; there are no ties. 
# Each team will compete against all other teams exactly once. Every time a team wins a competition, it gets 3 points; when it loses, it gets 0 points.
# It's guaranteed that the tournament always has at least two teams and there will be only one tournament winner.

# data = set()

competitions = [["HTML","C#"],["C#","Python"],["Python","HTML"]]
results = [0,0,1]
        
def tournamentWinner(competitions, results):
    bestTeam = ""
    scores = {bestTeam : 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition # Split array into 2

        winningTeam = homeTeam if result == 1 else awayTeam

        updateScores(winningTeam, scores)

        if scores[winningTeam] > scores[bestTeam]:
            bestTeam = winningTeam
    return bestTeam

def updateScores(team, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += 3

        

        
print(tournamentWinner(competitions,results))
        


