import random

class Deck():
    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
        self.deck = []
        for suit in suits:
            for rank in ranks:
                name = '%s of %s' % (rank, suit)
                if rank in ['J', 'Q', 'K']:
                    rank = 10
                if rank == 'A':
                    rank = 11
                self.deck.append([name,rank])

    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def show_deck(self):
        print(self.deck)
        print(len(self.deck))


class Hand():
    def __init__(self):
        self.cards = []
        self.point_value = 0
        self.aces = 0

    def show(self):
        current_hand = []
        for card in self.cards:
            current_hand.append(card[0])
        #add more human readable format
        return 'Your hand: \n %s' % current_hand

    def hit(self, deck):
        self.cards.append((deck.pop()))
        if self.cards.append((deck.pop()))[0] == 'A':
            self.aces += 1

    def deal(self, deck):
        self.hit(deck)
        self.hit(deck)

    def ace_value(self):
        for index, card in enumerate(self.cards):
            if 'A' in card[index] and item[1] == 11:
                item[1] = 1
                break

    def points(self):
        for index, item in enumerate(self.cards):
            self.point_value += self.cards[index][1]

    def is_blackjack(self):
        if len(self.cards) == 2 and self.point_value == 21:
            print('Black Jack! \n sum is: %i' % self.point_value)
            return True
        elif self.point_value == 21:
            print('Black Jack! \n sum is: %i' % self.point_value)
            return True
        elif self.point_value > 21:
            print('Bust... \n sum is: %i' % self.point_value)
            print('You loose.')
            return True
        else:
            return False


class Bet():
    pass


if __name__ == '__main__':
    game_over = False
    play_again = True
    while play_again:
        game = Deck()
        player = Hand()
        game.shuffle()
        player.deal(game.deck)
        while not game_over:
            print(player.show())
            if player.is_blackjack():
                game_over = True
                break
            while raw_input('What would you like to do? (hit,stay) ').lower() != 'stay':
                player.hit(game.deck)
                print(player.show())
                if player.is_blackjack():
                    game_over = True
                    break
        if raw_input('Would you like to play again? \'yes\'? ').lower() == 'yes':
            play_again = True
            game_over = False
        else:
            play_again = False
