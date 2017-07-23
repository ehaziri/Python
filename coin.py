import random
heads = 0
tails = 0
for i in range(0,5001):
    random_num = random.random()
    rounded = round(random_num)
    print(rounded)
    if(rounded == 1.0):
        heads += 1
        print("Attempt", i, ": Throwing a coin...It's a head!...Got", heads, " head(s) so far and", tails, " tail(s) so far")

    else:
        tails += 1
        print("Attempt", i, ": Throwing a coin...It's a tail!...Got", heads, " head(s) so far and", tails, " tail(s) so far")
