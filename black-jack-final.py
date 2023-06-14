import random

print("*************welcome to black-jack game***************")
cards = {"ace":11,
         "2" :2 ,
         "3" : 3,
         "4" : 4,
         "5" :5 ,
         "6" :6 ,
         "7" :7 ,
         "8" :8 ,
         "9" :9 ,
         "10": 10,
         "jack":10,
         "king":10,
         "queen":10}

deck = list(cards.keys())*4
# print(deck)

player_hand = []
dealer_hand = []

def card(hand):
    hand = random.choice(deck)
    return hand


while True:
    ##player side
    player = [card(player_hand), card(player_hand)]
    player_hand.append(player)
    ##casino side
    dealer = [card(dealer_hand), card(dealer_hand)]
    dealer_hand.append(dealer)
    dealer_str = [dealer[0], "*"]
    ##show first cards
    print("------- dealer cards: ",dealer_str, "\n-------", "player cards: ", player)
    
    # cards value
    player_sum = sum([cards[card] for card in player])#list comprehension
    dealer_sum = sum([cards[card] for card in dealer])
    print("dealer sum is:", dealer_sum,"\n",  "player sum is:", player_sum)
    response = input("stand or hit  : (s/h)").lower()
    
    while response in {"h", "s"}:
        #user input
        if response == "s":
            dealer_rand = "hit" #random.choice(["pass", "hit"])
            print("----dealer choice is :", dealer_rand)
            if dealer_rand == "hit":
                new_card = card(dealer_hand) 
                dealer_hand.append(new_card)
                # deck.remove(new_card)
                print( "dealer new card is: ", new_card)
                dealer_sum += cards[new_card]
                if  17 < dealer_sum < 21:
                    if dealer_sum > player_sum:
                        print("dealer win!!!!!!!!!!!")
                        break
                    elif dealer_sum == player_sum:
                        print("ooooohhhh its draw")
                        break
                    else:
                        print("player win !!!!!!!!!!!!")
                        break
                print("dealer cards sum is: ", dealer_sum)
            else:# dealer select PASS
                print("---- dealer PASS ----")
                response = input("stand or hit  : (s/h)").lower()
                continue
                
        
        else: # response == "h":
            new_card = card(player_hand) 
            player_hand.append(new_card)
            
            print( "player new card is: ", new_card)
            player_sum += cards[new_card]
            print(player_sum)
            
        
        if player_sum > 21 or dealer_sum > 21:
            break
        
        else:
            response = input("stand or hit  : (s/h)").lower()
            continue
        
        
    else:
        print("enter a single letter  S/H:")   
    
    if player_sum ==21 and dealer_sum == 21:
               
        print("oooohhhh its draw ")
        
    
    elif player_sum ==21:
        print(f"player win**********and sum is {player_sum}")
        
    
    elif dealer_sum == 21:
        print(f"dealer win**********and sum is {dealer_sum}")
        
        
         
    
    elif player_sum > 21:
        print(f"------its over 21 player lost, sum :{player_sum}")
        
    
    elif dealer_sum > 21:
        print(f"-------its over 21 dealer lost, sum: {dealer_sum}")
        
    
    else:
        if dealer_sum > player_sum:
            print(f"dealer win!!!!!!!and sum is {dealer_sum}")
        else:
            print(f"player win !!!!!!! and sum is {player_sum}")
    
    
    #repeat game
    r = input("do you wanna play again:  Y/N=   ").lower()
    
    while r  not in {"y", "n"}:
        print("enter a single letter  Y / N :  ")
        r = input("do you wanna play again:  Y/N=   ").lower() 
        
            
        
        
    else:
        if r == "y":
            continue
        else:
            pass
        
    
    
    
    
    break

print("player_hand: ", player_hand )
print("dealer_hand: ", dealer_hand )


