import random
def coin_flip():
    return random.choice(['Heads',"Tails"])
head=0
tails=0
n=int(input("how many times do you want to flip the coin?"))
for _ in range(n):
    result=coin_flip()
    if result=="Heads":
        head+=1
    else:
        tails+=1
        print(f"heads: {head}")
        print(f"tails: {tails}")

