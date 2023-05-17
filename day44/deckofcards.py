import random
from card import Card

class DeckOfCards:
    NUMBERS_OF_CARDS = 52
    def __init__(self) -> None:
        self._current_card = 0
        self._deck = []
        
        for count in range(DeckOfCards.NUMBERS_OF_CARDS):
            self._deck.append(Card(Card.FACES[count%13], Card.SUITS[count//13]))
            
    def shuffle(self):
        self._current_card = 0
        random.shuffle(self._deck)
        
    def deal_card(self):
        try:
            card = self._deck[self._current_card]
            self._current_card+=1
            return card
        except:
            return None
        
    def __str__(self) -> str:
        s = ""
        for index, _ in enumerate(self._deck):
            s += f" {self._deck[index]:<14} "
            if (index+1)%13 == 0:
                s += "\n"
        return s