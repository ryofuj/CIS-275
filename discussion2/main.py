from discussion2 import GolfScore

def main():
    par = int(input("Enter the par: "))
    score1 = int(input("Enter the score of player 1: "))
    score2 = int(input("Enter the score of player 2: "))
    score3 = int(input("Enter the score of player 3: "))
    
    print(GolfScore(par, score1, score2, score3))

main()