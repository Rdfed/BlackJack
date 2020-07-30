'''
This is the Deck class defined for the BlackJack Game
'''
#***************************************************************************************************************************************
#--------------------------------------------------------import Modules ----------------------------------------------------------------
import CardClass
import random
#***************************************************************************************************************************************
#--------------------------------------------------------    Class   ---------------------------------------------------------------
class Deck():
	def __init__(self):
		self.the_deck = []
		for i in CardClass.suits:
			for j in  CardClass.ranks:
				self.the_deck.append(CardClass.Card(i,j))
	def shuffle(self):
		random.shuffle(self.the_deck)
		#k = random.sample(self.the_deck,len(self.the_deck))
		#return k

	def __str__(self):
		return self.the_deck

	def pick_one(self):
		return self.the_deck.pop()
#****************************************************************************************************************************************
#------------------------------------------------------- Test - Statements --------------------------------------------------------------
if __name__ == '__main__':
	A = CardClass.Card(CardClass.suits[0],CardClass.ranks[0])
	print(A)
	new_deck = Deck()
	new_deck.shuffle()
	print(new_deck.the_deck[36])
	print(len(new_deck.the_deck))
	z = new_deck.pick_one()
	print(z)
	print(len(new_deck.the_deck))
#****************************************************************************************************************************************
