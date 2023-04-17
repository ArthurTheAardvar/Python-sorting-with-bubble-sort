import random

#i know their was a better way to do this i just wanted to finish this code
bubble = [random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12), random.randrange(0,12)]
print(bubble)




for j in range(9):
    for i in range(0, 10):
        if bubble[i] > bubble[i+1]:
            bubble[i], bubble[i+1] = bubble[i+1], bubble[i]

print(bubble)