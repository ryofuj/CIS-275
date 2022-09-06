"""
Ryo Fujimura
Discussion 2

Golf Score
user inputs Par
user inputs Score of player 1, 2, 3
Compare the scores of the players
print the winner and score
"""

class GolfScore:
    def __init__(self, par, score1, score2, score3):
        '''
        Constructor
        '''
        self.par = par
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    
    def __sb__(self, other):
       '''
       subtract the par from the score
       '''
       return self.score1 - self.par

    def __str__(self):
        '''
        overload the string method
        '''
        if self.score1 - self.par < self.score2 - self.par and self.score1 - self.par < self.score3 - self.par:
            return "Player 1 wins!" + " Score: " + str(self.score1 - self.par)
        elif self.score2 - self.par < self.score1 - self.par and self.score2 - self.par < self.score3 - self.par:
            return "Player 2 wins!" + " Score: " + str(self.score2 - self.par)
        elif self.score3 - self.par < self.score1 - self.par and self.score3 - self.par < self.score2 - self.par:
            return "Player 3 wins!" + " Score: " + str(self.score3 - self.par)
        else:
            return "Tie!"