import random
from card import Card

class DeckOfCards:
    NUMBERS_OF_CARDS = 52
    def __init__(self) -> None:
        self._current_card = 0
        self._deck = []    
        for count in range(DeckOfCards.NUMBERS_OF_CARDS):
            self._deck.append(Card(Card.FACES[count%13], Card.SUITS[count//13]))
        self.gendeal = self.deal_card_gen()
            
    def shuffle(self):
        self._current_card = 0
        self.gendeal = self.deal_card_gen()
        random.shuffle(self._deck)
    
    @property
    def dealed_card(self):
        return next(self.gendeal)    
    
    def deal_card_gen(self):
        for card in self._deck:
            yield card

        
    def __str__(self) -> str:
        s = ""
        for index, _ in enumerate(self._deck):
            s += f" {self._deck[index]:<14} "
            if (index+1)%13 == 0:
                s += "\n"
        return s