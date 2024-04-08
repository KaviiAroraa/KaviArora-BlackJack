import random

ace = ['AD', 'AS', 'AC', 'AH']
king = ['KD', 'KS', 'KC', 'KH']
queen = ['QD', 'QS', 'QC', 'QH']
jack = ['JD', 'JS', 'JC', 'JH']
two = ['2D', '2S', '2C', '2H']
three = ['3D', '3S', '3C', '3H']
four = ['4D', '4S', '4C', '4H']
five = ['5D', '5S', '5C', '5H']
six = ['6D', '6S', '6C', '6H']
seven = ['7D', '7S', '7C', '7H']
eight = ['8D', '8S', '8C', '8H']
nine = ['9D', '9S', '9C', '9H']
ten = ['10D', '10S', '10C', '10H']

deck = [ace, king, queen, jack, two, three, four, five, six, seven, eight, nine, ten]

def calculate_total(cards):
    total = 0
    num_aces = 0

    for card in cards:
        if card in king or card in queen or card in jack:
            total += 10
        elif card in two:
            total += 2
        elif card in three:
            total += 3
        elif card in four:
            total += 4
        elif card in five:
            total += 5
        elif card in six:
            total += 6
        elif card in seven:
            total += 7
        elif card in eight:
            total += 8
        elif card in nine:
            total += 9
        elif card in ten:
            total += 10
        elif card in ace:
            total += 11
            num_aces += 1

    #Logic for using ace as 1 or 11
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1

    return total

def game():
    i = 0
    k = 0
    
    player = []
    dealer = []
    hidden = []
    reveal = []
    
    total = 0
    dealer_total = 0

    while True:
        if i == 0:
            for j in range(2):
                player_card = deck[random.randint(0, 12)][random.randint(0, 3)]
            
                if player_card not in player and player_card not in dealer:
                    player.append(player_card)
            i += 1
            print("Your cards: ", player)
            total = calculate_total(player)
            print("Your total: ", total)
            print()

        else:
            player_card = deck[random.randint(0, 12)][random.randint(0, 3)]
            
            if player_card not in player and player_card not in dealer:
                player.append(player_card)
                print("Your cards: ", player)
                total = calculate_total(player)
                print("Your total: ", total)
                print()

                print("Dealer cards: ", hidden)
                dealer_total = calculate_total(dealer)
                print()
        if total > 21:
            print("BUST! Dealer wins!")
            print()
            break

        if k == 0:
            l = 0
            while True:
                if l == 0:
                    dealer_card = deck[random.randint(0, 12)][random.randint(0, 3)]

                    if dealer_card not in player and dealer_card not in dealer:
                        dealer.append(dealer_card)
                        hidden.append(dealer_card)
                        dealer_total = calculate_total(dealer)
                else:
                    dealer_card = deck[random.randint(0, 12)][random.randint(0, 3)]

                    if dealer_card not in player and dealer_card not in dealer:
                        dealer.append(dealer_card)
                        hidden.append("X")
                        dealer_total = calculate_total(dealer)
                        print()
                l += 1
                if l > 1:
                    break
                
            print("Dealer cards: ", hidden)
            k += 1
        else:
            if dealer_total <= total:
                dealer_card = deck[random.randint(0,12)][random.randint(0,3)]
                if dealer_card not in player and dealer_card not in dealer:
                    dealer.append(dealer_card)
                else:
                    continue
            elif dealer_total > total and dealer_total < 21:
                dealer_card = deck[random.randint(0,12)][random.randint(0,3)]
                if dealer_card not in player and dealer_card not in dealer:
                    dealer.append(dealer_card)
                else:
                    continue
            
            
        if dealer_total > 21:
            print("DEALER BUST! You win!")
            break
        
        elif dealer_total < 21:
            choice = input("Would you like to hit or stay?: ")
            print()
            if choice.upper() == "HIT":
                continue
            else:
                print("Dealer hits.")
                print("Dealer cards: ", dealer)
                print("Dealer total: ", dealer_total)
                print()
                while True:
                    if dealer_total <= total:
                        dealer_card = deck[random.randint(0,12)][random.randint(0,3)]
                        if dealer_card not in player and dealer_card not in dealer:
                            dealer.append(dealer_card)
                        else:
                            continue
                        print("Dealer cards: ", dealer)
                        dealer_total = calculate_total(dealer)
                        print("Dealer total: ", dealer_total)
                        print()
                        
                        
                    if dealer_total > total or dealer_total == 21:
                        break
                        
                if dealer_total > 21:
                    print("DEALER BUST! You win!")
                else:
                    print("Dealer stays.")
                    print()

                if dealer_total == total:
                    print("You tie!")
                elif dealer_total > total and dealer_total <= 21:
                    print("Dealer wins!")
                else:
                    print("You win!")
                break
    print("Your total: ", total)
    print("Dealer total: ", dealer_total)
    print()
    print("Thanks for playing!")

print()
print("Welcome to black jack!")
print("Objective: get as close to a total of 21 as possible.")
print("If your total crosses 21, dealer automatically wins.")
print("Value of all face cards is 10, for ace it can be 1 or 11.")
print()
print("How to play: ")
print("In the first turn, 2 cards are dealed to you and to the dealer.")
print("Only one of the dealer's cards are revealed.")
print("The hidden card is revealed after you STAY. ")
print("hit - you want another card to be dealed to you.")
print("stay - you are satisfied with your total and want to stop.")
print()

start = input("Enter any key to begin: ")
print()
if start != '':
    game()
