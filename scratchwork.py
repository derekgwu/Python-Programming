#blackjack
import random
deck = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
current_hand = 0



def generate_card():
    idx = random.randrange(0,len(deck))
    card = deck[idx]
    print("Card Drawn: " + str(card))
    if card == "J" or card == "Q" or card == "K":
        card = 10
    if card == "A":
        card = 11

    return card


#simulate endless turns
while True:
    
    print("Current Hand Value: " + str(current_hand))
    move = input("Type Y To Hit, N To Stay\n")

    if move == "Y":
        current_hand += generate_card()
        if current_hand >= 21:
            print("YOU LOSE")
            break

    elif move == "N":
        if current_hand + generate_card() <= 21:
            print("YOU LOSE, you stayed under 21")
            break
        else:
            print("YOU WIN, good call!")
            break
        
    print("\n")

