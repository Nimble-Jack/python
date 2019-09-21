import random

class Deck():
    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        #ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
        ranks = [1,2,3,'K','A']
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

    def points(self):
        # calculates the points everytime
        self.point_value = 0
        for index, card in enumerate(self.cards):
            self.point_value += self.cards[index][1]

    def check_and_show(self):
        # Shows hand in easy to read format
        # calls points()
        # adjusts Ace's to 1's if over 21
        current_hand = []
        s = ', '
        for card in self.cards:
            current_hand.append(card[0])
        Hand.points(self)
        while self.point_value > 21 and self.aces > 0:
            Hand.ace_value_to_1(self)
            Hand.points(self)
            self.aces -= 1
        return 'Your hand: %s \nYour points: %i' % (s.join(current_hand),self.point_value)

    def hit(self, deck):
        # draws a card from deck and checks if it's an Ace
        self.cards.append((deck.pop()))
        if self.cards[-1][0][0] == 'A':
            self.aces += 1

    def deal(self, deck):
        self.hit(deck)
        self.hit(deck)

    def ace_value_to_1(self):
        # check if an Ace is in self.cards and changes it to 1
        for card in self.cards:
            if card[1] == 11:
                card[1] = 1
                break

    def is_blackjack(self):
        if len(self.cards) == 2 and self.point_value == 21:
            print('Black Jack!')
            return True
        elif self.point_value == 21:
            print('Black Jack!')
            return True
        elif self.point_value > 21:
            print('Bust...You loose.')
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
            player.check_and_show()
            print(player.check_and_show())
            if player.is_blackjack():
                game_over = True
                break
            while raw_input('What would you like to do? (hit,stay) ').lower() != 'stay':
                player.hit(game.deck)
                player.check_and_show()
                print(player.check_and_show())
                if player.is_blackjack():
                    game_over = True
                    break
            # do something if stay
        if raw_input('Would you like to play again? \'yes\'? ').lower() == 'yes':
            play_again = True
            game_over = False
        else:
            play_again = False
