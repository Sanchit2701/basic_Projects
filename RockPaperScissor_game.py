#rock paper scissor Project 
import random 

input=input("what your choice(rock,paper,scissor): ")

computer_inpt=random.choice(['rock','paper','scissor'])
print("computer choice(rock,paper,scissor) is :",computer_inpt)
if input==computer_inpt:
    print("draw")
elif input=='rock' and computer_inpt=="paper":
    print("computer wins")
elif input=='rock' and computer_inpt=="scissor":
    print("You wins")
elif input=='scissor' and computer_inpt=="paper":
    print("You wins")
elif input=='scissor' and computer_inpt=="rock":
    print("computer wins")
elif input=='paper' and computer_inpt=="rock":
    print("You wins")
elif input=='paper' and computer_inpt=="scissor":
    print("computer wins")

