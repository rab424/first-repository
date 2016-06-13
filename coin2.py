import random


x = int(input("How many times would you like to flip a coin? "))
def coinflip(x):
    heads = 0
    tails = 0
    i = 0
    while i < x:

        coin = random.randint(1, 2)

        if coin == 1:
            heads += 1
            i += 1

        elif coin == 2:
            tails += 1
            i += 1
    per_heads = (heads / x) * 100
    per_tails = (tails / x) * 100
    print("You flipped the coin %d times." % x)
    print("Out of %d flips, you got heads %d times and tails %d times." % (x, heads, tails))
    print("Your percentage heads was %.1f%%, and your percentage tails was %.1f%%." % (per_heads, per_tails))

coinflip(x)
