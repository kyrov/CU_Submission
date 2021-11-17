class Card:
    def __init__(self,value,suit):
        self.suit = suit
        self.value = value
    def getScore(self):
        if self.value == "A":
            return 1
        elif self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return int(self.value)
    def sum(self,other):
        return (self.getScore() + other.getScore())%10
    def __str__(self):
        return "(" + self.value + " " + self.suit + ")"
    def __lt__(self,rhs):
        if(self.value == rhs.value):
            order1 = {"club":1, "diamond":2, "heart":3, "spade":4}
            return order1[self.suit] < order1[rhs.suit]
        else:
            order2 = {"A":12, "J":9, "Q":10, "K":11, "2":13, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7 , "10": 8}
            return order2[self.value] < order2[rhs.value]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])