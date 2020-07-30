'''
Driver proram of BlackJack Game
'''
#***************************************************************************************************************************************
#--------------------------------------------------------import Modules ----------------------------------------------------------------
import CardClass
import DeckClass
import PlayerClass
import DealerClass
import DisplayModule
import random
import time
#***************************************************************************************************************************************
#--------------------------------------------------------Global Variables---------------------------------------------------------------
#***************************************************************************************************************************************
#--------------------------------------------   inital cards to player and Dealer  -----------------------------------------------------
def initial_cards(create_deck,player_name,player_cards,dealer_cards):
	for i in range(0,2):
		k = create_deck.pick_one()
		player_cards.append(k)
		k = create_deck.pick_one()
		dealer_cards.append(k)
	#DisplayModule.display3(1,2,'DEALER')
	#DisplayModule.display3(9,2,player_name)
	DisplayModule.display2(1,1,'DEALER',dealer_cards)
	DisplayModule.display4(9,2,player_name,player_cards)
	return (player_cards,dealer_cards)
#***************************************************************************************************************************************
#----------------------------------------------------  input player function  ----------------------------------------------------------
def player_details():
	player_name = input(' Enter your name   :  ')
	player_coins = 500     # Default value
	dealer_coins = 500000    # Default value
	return (player_name,player_coins,dealer_coins)

#***************************************************************************************************************************************
#----------------------------------------------------   Betting  function   ------------------------------------------------------------

def betting(player_name,player_coins):
	betted_coins = 10
	while betted_coins % 50 != 0:
		while True:
			try:
				betted_coins = int(input(' Enter the bet in mulitples of 50 : '))
			except ValueError:
				print(" OOPS! Thats not a integer, try again...")
				continue
			else:
				break
		if betted_coins > player_coins:
			print(" \n Sorry insufficient balance  ")
			betted_coins = 10
			continue
		elif betted_coins % 50 == 0:
			return betted_coins
		else:
			print(" \n Please Enter your bet in the multiples of 50  [50 100 150 200 .. ] : ")
#***************************************************************************************************************************************
#--------------------------------------------------     Plyaer Ace 1 or 11   -----------------------------------------------------------
def player_ace_one_or_eleven(k):
	if k.rank == 'Ac':
		choice = 30   # Any random value other than 1 and 11
		while choice not in [1,11]:
			choice = int(input('You got an ACE ...... 1 or 11 ??    :  '))
			if choice == 1 or choice == 11:
				return choice
			else:
				print(" Invalid selection..... ACE can be either 1 or 11 ")
	else:
		print(" Incorrect funcion call ...!!!....This function is dedicated for Ace card only")

#***************************************************************************************************************************************
#--------------------------------------------------     Dealer Ace 1 or 11   -----------------------------------------------------------
def dealer_ace_one_or_eleven(k,dealer_value):
	if k.rank == 'Ac':
		if ((dealer_value + 11) > 21):
			k.value = 1
		elif ((dealer_value + 11) <= 21) and ((dealer_value + 11) > 17):
			k.value = 11
		else:
			z = [1,11]
			k.value = random.choice(z)
		return k.value		
	else:
		print(" Incorrect funcion call ...!!!....This function is dedicated for Ace card only")
#***************************************************************************************************************************************
#--------------------------------------------------        Ace Check         -----------------------------------------------------------
def ace_check(k):
	if k.rank == 'Ac':
		return True
	else:
		return False
#***************************************************************************************************************************************
#--------------------------------------------------Player Stand or Hit   ---------------------------------------------------------------
def player_stand_or_hit(player_name,create_deck,player_sum,player_coins,dealer_coins,betted_coins,player_cards):
	choice = 'k'   # Any value other than H or S
	n = 2
	while choice != 's':
		print(f'Hi {player_name}, What would you choose ?? ')
		choice = input(" \n ***  HIT or STAND (H/S) *** : ")
		if choice.lower() == 'h':
			time.sleep(1)
			k = create_deck.pick_one()
			player_cards.append(k)
			DisplayModule.display5(9,n+1,player_name,player_cards)
			choice1 = ace_check(player_cards[n])
			if choice1 == True:
				player_cards[n].value = player_ace_one_or_eleven(player_cards[n])
			player_sum = player_sum + player_cards[n].value
			n = n+1
			if player_sum > 21:
				#print(f"Your score is {player_sum}")
				print(f" You lost {betted_coins} coins")
				print(" \n *** GAME OVER !!! ***")
				dealer_coins = dealer_coins + betted_coins
				player_coins = player_coins - betted_coins
				DisplayModule.display1(player_name,player_coins,dealer_coins)
				return (False,player_sum,dealer_coins,player_coins,player_cards)
			else:
				pass
		elif choice.lower() == 's':
			#print(f"Your score is {player_sum}")
			return (True,player_sum,dealer_coins,player_coins,player_cards)
		else:
			print(" Wrong input!!! please select either H or S :")
#***************************************************************************************************************************************
#-------------------------------------------------------   Dealer Turn   ---------------------------------------------------------------
def dealer_turn(dealer_cards,dealer_sum,player_sum,player_name,player_coins,dealer_coins,betted_coins,create_deck):
	DisplayModule.display4(1,2,'DEALER',dealer_cards)
	choice3 = ace_check(dealer_cards[0])
	if choice3 == True:
		dealer_cards[0].value = dealer_ace_one_or_eleven(dealer_cards[0],0)
	choice4 = ace_check(dealer_cards[1])
	if choice4 == True:
		dealer_cards[1].value = dealer_ace_one_or_eleven(dealer_cards[1],dealer_cards[0].value)
	dealer_sum = len(dealer_cards[0]) + len(dealer_cards[1])
	if (dealer_sum > player_sum) and (dealer_sum <= 21):
		print(f'{player_name} lost {betted_coins} coins')
		player_coins = player_coins - betted_coins
		dealer_coins = dealer_coins + betted_coins
		DisplayModule.display1(player_name,player_coins,dealer_coins)
		return (player_sum,dealer_coins,player_coins)
	n1 = 2
	while dealer_sum < player_sum:
		z = create_deck.pick_one()
		dealer_cards.append(z)
		time.sleep(3)
		DisplayModule.display5(1,n1+1,'DEALER',dealer_cards)
		choice5 = ace_check(dealer_cards[n1])
		if choice5 == True:
			dealer_cards[n1].value = dealer_ace_one_or_eleven(dealer_cards[n1],dealer_sum	)
		dealer_sum = dealer_sum + dealer_cards[n1].value
		n1 = n1 + 1
	if (dealer_sum > player_sum) and (dealer_sum <= 21):
		print(f'{player_name} lost {betted_coins} coins')
		player_coins = player_coins - betted_coins
		dealer_coins = dealer_coins + betted_coins
		DisplayModule.display1(player_name,player_coins,dealer_coins)
		return (player_sum,dealer_coins,player_coins)
	elif (dealer_sum == player_sum):
		print(" \n *** MATCH TIED ***")
		DisplayModule.display1(player_name,player_coins,dealer_coins)
		return (player_sum,dealer_coins,player_coins)
	elif dealer_sum > 21 :
		print(f'{player_name} won {betted_coins} coins')
		player_coins = player_coins + betted_coins
		dealer_coins = dealer_coins - betted_coins
		DisplayModule.display1(player_name,player_coins,dealer_coins)
		return (player_sum,dealer_coins,player_coins)
#***************************************************************************************************************************************
#-------------------------------------------------------   Main Function   ---------------------------------------------------------------
def main(player_coins,player_name,dealer_coins,create_deck,player_cards,dealer_cards,player_sum,dealer_sum):
	if player_coins == 0:
		print(" Sorry you lost all the money !!! ")
		exit(0)
	betted_coins = betting(player_name,player_coins)
	DisplayModule.display6(betted_coins)
	time.sleep(1)
	(player_cards,dealer_cards) = initial_cards(create_deck,player_name,player_cards,dealer_cards)
	choice1 = ace_check(player_cards[0])
	if choice1 == True:
		player_cards[0].value = player_ace_one_or_eleven(player_cards[0])
	choice2 = ace_check(player_cards[1])
	if choice2 == True:
		player_cards[1].value = player_ace_one_or_eleven(player_cards[1])
	player_sum = len(player_cards[0]) + len(player_cards[1])
	(f,player_sum,dealer_coins,player_coins,player_cards) = player_stand_or_hit(player_name,create_deck,player_sum,player_coins,dealer_coins,betted_coins,player_cards)
	if f == True:
		(player_sum,dealer_coins,player_coins) = dealer_turn(dealer_cards,dealer_sum,player_sum,player_name,player_coins,dealer_coins,betted_coins,create_deck)
		time.sleep(1)
		replay_func(player_coins,dealer_coins)
	elif f == False:
		time.sleep(1)
		replay_func(player_coins,dealer_coins)
#***************************************************************************************************************************************
#------------------------------------------------------- Replay Funciton ---------------------------------------------------------------
def replay_func(player_coins,dealer_coins):
	replay = 'z' # any random value  other than 'y' or 'n'
	while replay not in ['y','n']:
		replay = input('Wanna play again (Y/N)  ??   : ')
		if replay.lower() == 'y':
			create_deck1 = DeckClass.Deck()
			create_deck1.shuffle()
			player_cards = []
			dealer_cards = []
			player_sum = 0
			dealer_sum = 0
			main(player_coins,player_name,dealer_coins,create_deck1,player_cards,dealer_cards,player_sum,dealer_sum)
		elif replay.lower() == 'n':
			print(f" Have a nice day {player_name}, see you again")
			exit(0)
		else:
			print('OOPS!!! ..... INVALID input ')		
#***************************************************************************************************************************************
#------------------------------------------------------- Driver Funciton ---------------------------------------------------------------
if __name__ == '__main__':
	(player_name,player_coins,dealer_coins) = player_details()
	player_cards = []
	dealer_cards = []
	player_sum = 0
	dealer_sum = 0
	DisplayModule.display0()
	DisplayModule.display1(player_name,player_coins,dealer_coins)
	create_deck = DeckClass.Deck()
	create_deck.shuffle()
	main(player_coins,player_name,dealer_coins,create_deck,player_cards,dealer_cards,player_sum,dealer_sum)
	#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#***************************************************************************************************************************************