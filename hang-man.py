#  HANG-MAN GAME
import random
from pathlib import Path
# import re

path1 = Path('random-words.txt')
words = path1.read_text()
words = words.split()
# print(words)##its work
goal = random.choice(words)
goal = goal.lower()
goal_len = len(goal)

# path2 = Path('HANGMANPICS.py')
# hang = path2.read_text()
# hang = "".join(hang)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# print(HANGMANPICS[1])

# global health
# health = len(HANGMANPICS)
# print(health)
def win():
    print("congratulation !!!!!!! you win")
    
def lost():
    print("ooooohhhh!!!  you losse  ")
    
# answer = re.sub(".", "_", goal)
# print(answer)
print(f"the answer is >> {goal_len} << character")
goal_set = set(goal)
print(goal)
# print(re.sub("." , "a" ,answer ))

# user_input = str(input("input a letter: ")).lower()
# print(user_input)

###ERROR HANDLING##########
alphabet = "abcdefghijklmnopqrstuvwxyz"
user_input_list = []

hang = 0
health = 6
word = "_"* goal_len
print("welcome to HANGMAN")

while health:
    #USER INPUT
    user_input = str(input("input a letter: ")).lower()           
       
    if user_input in alphabet: 
        
        if user_input in goal:
            # IT'S OK
            for i, char in enumerate(goal):
                if user_input == char:
                    if user_input in user_input_list:
                        print("You have already entered this character")
                        continue
                    else:    
                        goal_set.remove(user_input)
                        user_input_list.append(char)
                        word = word[:i] + char + word[i+1:]
                        print(word)
                        print(user_input_list)
                      
                else:
                    print("_", end = "")
                
            print("\n.................................................................")
        
        else:
            health -= 1
            hang += 1
            print(HANGMANPICS[hang])
            print("health is: " ,health)
            if health == 0:         
                lost()
                break
            
    else:
        print("enter a valid letter A - Z:")
        continue
    
    print(goal_set)
    
    if not goal_set:
        win()
        break
    
        
        
















#  WHILE LOOP  #
# health = 0
# while True:
#     if health < len(HANGMANPICS):
#         for i in HANGMANPICS:
#             user_input = input("input a letter: ").lower()
#             if user_input.exist(goal):
#                 #replace letter in goal expression
#                 pass
#             else:
#                 pass
            




























