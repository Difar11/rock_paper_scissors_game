# rock_paper_scissors_game
import random

possible_actions = ["akmens" , "šķēres" , "papīrs"]

human_turn = 'akmens'
computer_turn = random.choice(possible_actions)

if human_turn == computer_turn :
    print("gandrīz vins\n"*20)
elif human_turn == 'papīrs' and computer_turn == 'šķēres':
    print("viņš čīto\n"*20) 
elif human_turn == 'akmens' and computer_turn == 'papīrs':
    print("viņš čīto\n"*20) 
elif human_turn == 'šķēres' and computer_turn == 'akmens':
    print("viņš čīto\n"*20) 
else :
    print("gg ez\n"*20) 
