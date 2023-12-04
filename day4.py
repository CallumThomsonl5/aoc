# win | you have
f = open("day4.txt")
inp = f.read().split("\n")

def sol1():
    total = 0

    for card in inp:
        wh = card.split(":")[1].split("|")
        win = [x for x in wh[0].strip().split(" ") if x]
        have = [x for x in wh[1].strip().split(" ") if x]
        total += int(2**(len(set(win).intersection(set(have))) - 1))

    print(total)

def sol2():
    total = 0
    copies = [1] * len(inp)

    for card_number, card in enumerate(inp):
        wh = card.split(":")[1].split("|")
        win = [x for x in wh[0].strip().split(" ") if x]
        have = [x for x in wh[1].strip().split(" ") if x]

        copies_won = len(set(win).intersection(set(have)))
        for j in range(copies_won):
            copies[card_number+1+j] += copies[card_number]
        
        total += copies[card_number]

    print(total)
