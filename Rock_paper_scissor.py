from random import choice
name = raw_input("Enter your name : ")
print "Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock"
rps = ['r','p','s']
user_score = 0
computer_score = 0

while 1:
    print "R: Rock,      P: Paper,     S: Scissor"
    user = raw_input("Enter your choice among the three : ")   
    user = user.lower()
    py = choice(rps)

    if user == py:
        print "You chose ",user
        print "I chose ",py
        print "Hence a Tie!"

    elif user == 'r' and py == 's':
        print 'You entered Rock. I had Scissor. You win!'
        user_score+=1
    elif user == 'r' and py == 'p':
        print 'You entered Rock. I had Paper. You lose!'
        computer_score+=1
    elif user == 's' and py == 'p':
        print 'You entered Scissor. I had Paper. You win!'
        user_score+=1
    elif user == 's' and py == 'r':
        print 'You entered Scissor. I had Rock. You lose!'
        computer_score+=1
    elif user == 'p' and py == 's':
        print 'You entered Paper. I had Scissor. You lose!'
        computer_score+=1
    elif user == 'p' and py == 'r':
        print 'You entered Paper. I had Rock. You win!'
        user_score+=1

    if computer_score== 5:
        print "The computer won the game"
        break
    elif user_score==5:
        print name+" won the game"
        break
