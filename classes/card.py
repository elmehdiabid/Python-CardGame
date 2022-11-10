class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank[self.rank] + self.suits[self.suits]    
    

    def __lt__(self, other):
        if self.suit != other.suit:
            return self.suit < other.suit
        return self.rank < other.rank







   

    
