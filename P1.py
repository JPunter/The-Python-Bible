import random

#dif 1 is easy, dif 2 is hard

dif = 6


HP = 50
potionHealth = int(random.randint(25/dif,50/dif))

HP = HP + potionHealth

print (HP)

