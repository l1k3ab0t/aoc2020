from collections import deque


deck1, deck2 = [deque(int(l) for l in deck.splitlines()) for deck in open("input").read().split("\n\n")]

print(deck1, deck2)


def play(deck1, deck2):
    while True:
        card1 = deck1.popleft()
        card2 = deck2.popleft()

        if card1 < card2:
            deck2.append(card2)
            deck2.append(card1)

        else:
            deck1.append(card1)
            deck1.append(card2)



        if len(deck1) == 0:
            deck2.reverse()
            return sum(map(lambda x: x[0]*x[1],  zip(list(deck2), range(1,len(deck2)+1))))
            
        if len(deck2) == 0:
            deck1.reverse()
            return sum(map(lambda x: x[0]*x[1],  zip(list(deck1), range(1,len(deck1)+1))))


def play_recursive(deck1, deck2, sub=False):

    prev_decks = set()

    while True:

        key = (tuple(deck1), tuple(deck2))
        if key in prev_decks:
            return False

        prev_decks.add(key)


        card1 = deck1.popleft()
        card2 = deck2.popleft()
    


        if len(deck1)>=card1 and len(deck2)>=card2:
            if play_recursive(deque(list(deck1)[:card1]), deque(list(deck2)[:card2]), True):
                deck2.append(card2)
                deck2.append(card1)
            else:
                deck1.append(card1)
                deck1.append(card2)

        else:
            if card1 < card2:
                deck2.append(card2)
                deck2.append(card1)

            else:
                deck1.append(card1)
                deck1.append(card2)



        if len(deck1) == 0:
            if sub:
                return True
            else:
                deck2.reverse()
                return sum(map(lambda x: x[0]*x[1],  zip(list(deck2), range(1,len(deck2)+1))))
            
        if len(deck2) == 0:
            if sub:
                return False
            else:
                deck1.reverse()
                return sum(map(lambda x: x[0]*x[1],  zip(list(deck1), range(1,len(deck1)+1))))



print("Part 1", play(deck1.copy(), deck2.copy()))
print("Part 2", play_recursive(deck1, deck2))
