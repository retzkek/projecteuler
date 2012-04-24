#!/usr/bin/python
# encoding: utf-8
class card:
    """
    represents a poker/playing card
    """
    suites = ['S','C','H','D']
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    def __init__(self,cardstr=None):
        if cardstr is None:
            self.suite=None
            self.value=None
        else:
            self.setcard(cardstr)
    def __str__(self):
        return self.values[self.value]+self.suites[self.suite]
    def setcard(self,cardstr):
        self.value = self.values.index(cardstr[0:1])
        self.suite = self.suites.index(cardstr[1:2])

class hand:
    """
    represents a five-card poker hand
    """
    hands = ['HIGH','PAIR','TWOPAIR','TRIPS','STRAIGHT','FLUSH',
             'FULLHOUSE','QUAD','STRAIGHTFLUSH']
    def __init__(self,cards=None):
        if cards is None:
            self.cards = None
        else:
            self.setCards(cards)
    def setCards(self,cards):
        """
        set the cards in the hand, as list of card objects
        """
        assert len(cards) == 5
        self.cards=[]
        for c in cards:
            self.cards.append(card(str(c)))
    def sets(self,nCardsInSet=2):
        """
        returns a list of the values of the sets of length nCardsInSet
        """
        uniques = set(self._valueList())
        s = []
        for c in uniques:
            if self._valueList().count(c) == nCardsInSet:
                s.append(c)
        return s
    def isStraight(self):
        """
        returns True if hand is a straight (or straight flush)
        """
        v = self._valueList()
        v.sort()
        for i in range(1,5):
            if v[i] != v[i-1]+1:
                return False
        return True
    def isFlush(self):
        """
        returns False if hand is a flush (or straight flush)
        """
        if self.cards[0].suite == self.cards[1].suite and \
           self.cards[1].suite == self.cards[2].suite and \
           self.cards[2].suite == self.cards[3].suite and \
           self.cards[3].suite == self.cards[4].suite:
            return True
        return False
    def value(self):
        """
        value returns the best hand from hands[] and a list of values where:
            0/HIGH            values of the cards (sorted desc)
            1/PAIR            values of pair and remaining cards
            2/TWOPAIR         values of the two pairs and remaining card
            3/TRIPS           valuse of the trips and remaining two cards
            4/STRAIGHT        values of the cards
            5/FLUSH           values of the cards
            6/FULLHOUSE       values of the (trip,pair)
            7/QUAD            values of the four-of-a-kind and remaining card
            8/STRAIGHTFLUSH   value of the cards
        """
        straight = self.isStraight()
        flush = self.isFlush()
        pairs = self.sets(2)
        trips = self.sets(3)
        quads = self.sets(4)
        values = self._valueList()
        values.sort()
        values.reverse()
        valueset = set(values)
        if straight and flush:
            # STRAIGHTFLUSH
            return (8,values)
        elif len(quads) > 0:
            # QUAD
            valueset.remove(quads[0])
            return (7,[quads[0],max(valueset)])
        elif len(trips) > 0 and len(pairs) > 0:
            # FULLHOUSE
            return (6,(trips[0],pairs[0]))
        elif flush:
            # FLUSH
            return (5,values)
        elif straight:
            # STRAIGHT
            return (4,values)
        elif len(trips) > 0:
            # TRIPS
            valueset.remove(trips[0])
            values = list(valueset)
            values.sort()
            values.reverse()
            return (3,trips+values)
        elif len(pairs) > 1:
            # TWOPAIR
            valueset.remove(pairs[0])
            valueset.remove(pairs[1])
            values = list(valueset)
            return (2,pairs+values)
        elif len(pairs) > 0:
            # PAIR
            valueset.remove(pairs[0])
            values = list(valueset)
            return (1,pairs+values)
        else:
            # HIGH
            return (0,values)
    def _valueList(self):
        values=[]
        for c in self.cards:
            values.append(c.value)
        return values
    def __cmp__(self,other):
        sh, sv = self.value()
        oh, ov = other.value()
        if sh < oh:
            return -1
        elif sh > oh:
            return 1
        else:
            for v1,v2 in zip(sv,ov):
                if v1 < v2:
                    return -1
                elif v1 > v2:
                    return 1
            return 0
    def __str__(self):
        s = ""
        for c in self.cards:
            s += str(c) + " "
        return s
