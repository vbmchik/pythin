class Card:
    FACES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["hearts", "diamonds", "clubs", "spades"]
    
    def __init__(self, face, suit) -> None:
        self._face = face
        self._suit = suit

    @property
    def face(self):
        return self._face
     
    @property
    def suit(self):
        return self._suit
    
    @property
    def image_name(self):
        return f"{self.suit}_{self.face}.png"
    
    def __repr__(self) -> str:
        return f"Card(face={self.face}, suit={self.suit})"

    def __str__(self) -> str:
        return f"{self.face} of {self.suit}"
    
    def __format__(self, format: str) -> str:
        return f"{str(self):{format}}"