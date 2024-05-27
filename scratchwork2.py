#blackjack
import random
deck = [2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
current_hand = 0


#generates a random card and returns the value of the card. (i.e if drew a K, return 10)
def generate_card():
    return 0


#simulate endless turns
while True:
    
    print("Current Hand Value: " + str(current_hand))
    move = input("Type Y To Hit, N To Stay\n")

    #if the user clicks yes, they draw a card and add the value to current__hand. If they go over the limit, they lose
    if move == "Y":
        0

    #if the user clicks no, they would theorectically draw a card. If they do not go over the limit with the theorectical draw, they lose. Else, they win
    elif move == "N":
        0
        
    print("\n")

