import random
import logging
logging.basicConfig(filename='cards.log', filemode='w',\
    format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)

log = logging.getLogger(__name__)




class War():
    """ INCOMPLETE example -- how can you build on this?"""
    def __init__(self):

        # refactoring: could reuse newDeck as tableau?
        self.newDeck = Deck()
        self.newDeck.shuffle()
        
        self.handOne = Hand()
        self.handTwo = Hand()
        self.tableau = Hand()
        log.debug('Created newDeck, handOne, handTwo and tableau instances')
        return

        
    def deal(self):
        while len(self.newDeck.cards) > 0:
            self.handOne.add_card(self.newDeck.draw_card()) # add one card to handOne
            self.handTwo.add_card(self.newDeck.draw_card())
            log.debug('Added to hands, {} left in deck'.format(len(self.newDeck.cards)))
        return

    def turn(self):
        # each hand draw its top card
        self.cardOne = self.handOne.cards.pop()
        self.cardTwo = self.handTwo.cards.pop()

        self.tableau.add_card(self.cardOne)
        self.tableau.add_card(self.cardTwo)
        log.debug('Drew two cards: {0} and {1}'.format(str(self.cardOne), str(self.cardTwo)))
        
        # check if the cards are equal
        # if it's true, then go to war
        # if it's false then see which is greater

        if self.cardOne.is_equal(self.cardTwo):
            # the code for war
            # we have draw three top cards from each hand
            # then draw the fourth top card from each and comapre
            # then either repeat or add the tableau randomly to the winner's hand
            # highly imperative style rather than functional
            self.message = "war!"
            for i in range(3):
                self.tableau.add_card(self.handOne.cards.pop())
                self.tableau.add_card(self.handTwo.cards.pop())
            
            # Call turn again, this time with more cards in tableau
            log.info("War! There are {} cards in tableau".format(len(self.tableau.cards)))
            self.turn()

        else:
            if self.cardOne.greater_than(self.cardTwo):
                # giving the cards to hand one
                self.message = "player 1 wins round"
                log.info('player 1 wins round and adds {} cards to their hand of {}'.format(len(self.tableau.cards),len(self.handOne.cards)))
                
                # add self.cardOne and self.cardTwo into self.handOne.cards
                # they must go onto the bottom of self.handOne.cards
                # and they must go onto the bottom in random order
                while len(self.tableau.cards) > 0:
                    self.handOne.cards.insert(0,self.tableau.draw_card())
                
                log.debug('player 1 has {} cards'.format(len(self.handOne.cards)))


            else:
                # give the cards to hand two
                self.message = "player 2 wins round"
                log.info('player 2 wins round and adds {} cards to their hand of {}'.format(len(self.tableau.cards),len(self.handTwo.cards)))
                
                while len(self.tableau.cards) > 0:
                    self.handTwo.cards.insert(0,self.tableau.draw_card())
                
                log.debug('player 2 has {} cards'.format(len(self.handTwo.cards)))

        return self.message

    # def play_game(self):

class Card():
    '''A standard playing card'''
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', \
                 '9', '10', 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], \
                            Card.suit_names[self.suit])
    
    def greater_than(self, other):
        # YOUR CODE HERE
        if other.rank == 1:
            return False            
        else:
            return self.rank > other.rank
        
    def is_equal(self, other):
        if self.rank == other.rank:
            return True
        else:
            return False

class Deck():
    '''52 unique cards. No jokers.'''
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        results = []
        for card in self.cards:
            results.append(str(card))
        return '\n'.join(results)
    
    def draw_card(self):
        '''Draws a random card'''
        c = random.choice(self.cards)
        self.cards.remove(c)
        return c
    
    def add_card(self, card):
        '''Puts a card object back in the deck'''
        self.cards.append(card)            
    
    def shuffle(self):
        '''Shuffles the deck'''
        random.shuffle(self.cards)

    def sort(self):
        '''Sorts the deck'''
        self.cards.sort()
        
class Hand(Deck):
    '''Empty for now'''
    def __init__(self):
        self.cards = []

if __name__ == "__main__":
    w = War()
    w.deal()
    counter = 0

    # sometimes this fails -- examine the log to see why!
    while (w.handOne.cards and w.handTwo.cards):
        counter+=1
        w.turn()
        if len(w.handOne.cards) + len(w.handTwo.cards) > 52: log.warning("Created more than 52 cards.")
        if counter > 10000:
            log.warning('possible infinite loop, breaking execution')
            break
    if w.handOne.cards:
        print 'player 1 won!'
    else:
        print 'player 2 won!'
    print len(w.handOne.cards), len(w.handTwo.cards)
