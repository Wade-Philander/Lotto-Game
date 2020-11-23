import random
from random import sample

num = sample(range(1,50),6)
print(num)

count = 0

print("WELCOME TO THE LOTTO DRAW!")
print("Please choose your 6 lucky lotto winning numbers below")

while count <= 7:
    count +=1
    print("Enter your")