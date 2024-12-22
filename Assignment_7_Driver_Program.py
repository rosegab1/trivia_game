#Gabriela Feliciano
#U60146452
'''The purpose of this program is to play a two-player trivia game and to
obtain the questions and answers from another module'''

from Assignment_7_Trivia_Questions import trivialist


player1score = 0
player2score = 0

for i, k in enumerate(trivialist()):
    if i % 2 == 0:
        print('Question for the first player:')
        print(k.getquestion())
        print('1.', k.getanswer1())
        print('2.', k.getanswer2())
        print('3.', k.getanswer3())
        print('4.', k.getanswer4())
        guess = int(input('Enter your solution (a number between 1 and 4): '))
        if guess == k.getcorrect():
            print('That is the correct answer.')
            player1score += 1
        else:
            print(f'That is incorrect. The correct answer is {k.getcorrect()}')
        print()
    elif i % 2 == 1:
        print('Question for the second player:')
        print(k.getquestion())
        print('1.', k.getanswer1())
        print('2.', k.getanswer2())
        print('3.', k.getanswer3())
        print('4.', k.getanswer4())
        guess = int(input('Enter your solution (a number between 1 and 4): '))
        if guess == k.getcorrect():
            print('That is the correct answer.')
            player2score += 1
        else:
            print(f'That is incorrect. The correct answer is {k.getcorrect()}')
        print()
        
print(f'The first player earned {player1score} points.')
print(f'The second player earned {player2score} points.')

if player2score == player1score:
    print('There was a tie!')
elif player1score > player2score:
    print('The first player wins the game.')
elif player2score > player1score:
    print('The second player wins the game.')
