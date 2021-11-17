class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def __str__(self):
        return "(" + self.value + " " + self.suit + ")"
    def next1(self):
        order1 = {"club":1, "diamond":2, "heart":3, "spade":4}
        order2 = {"A":12, "J":9, "Q":10, "K":11, "2":13, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7 , "10": 8}
        order3 = {1:'3',2:'4',3:'5',4:'6',5:'7',6:'8',7:'9',8:'10',9:'J',10:'Q',11:'K',12:'A',13:'2'}
        order4 = {1:"club", 2:"diamond", 3:"heart", 4:"spade"}
        a = order1[self.suit]
        b = order2[self.value]
        if(a == 4):
            a = 1
            b += 1
            if(b == 14):
                b = 1
        else:
            a += 1
        return Card(order3[b], order4[a])
    def next2(self):
        a = self.next1()
        self.value = a.value
        self.suit = a.suit
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])