import random

class Deck():
    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        #ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
        ranks = [9,'Q']
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
    def __init__(self,player_name):
        self.player_name = player_name
        self.cards = []
        self.point_value = 0
        self.aces = 0

    def points(self):
        # calculates the points everytime
        self.point_value = 0
        for index, card in enumerate(self.cards):
            self.point_value += self.cards[index][1]
        return self.point_value

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
        return '%s hand: %s \n%s points: %i' % (self.player_name,s.join(current_hand),self.player_name,self.point_value)

    def hit(self, deck):
        # draws a card from deck and checks if it's an Ace
        # the check for an Ace has to come AFTER the pop then append
        # then just check the newly appended card's first item's first character
        # aka my_list[-1][0][0]
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
            print('Bust...')
            self.point_value = 0
            return True
        else:
            return False

# TODO betting system
class Bet():
    pass


if __name__ == '__main__':
    game_over = False
    play_again = True
    while play_again:
        # Sets up a fresh game
        game = Deck()
        player = Hand('Your')
        dealer = Hand('Dealer')
        game.shuffle()
        player.deal(game.deck)
        dealer.deal(game.deck)
        # Starts game
        while not game_over:
            # Player
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
            # Dealer
            dealer.check_and_show()
            print(dealer.check_and_show())
            if dealer.is_blackjack():
                game_over = True
                break
            while dealer.points() < 17:
                dealer.hit(game.deck)
                dealer.check_and_show()
                print(dealer.check_and_show())
                if dealer.is_blackjack():
                    game_over = True
                    break
            # Game Winner
            if dealer.point_value > player.point_value or dealer.point_value == player.point_value:
                print('You loose!')
                game_over = True
            else:
                print('You win!')
                game_over = True
        if raw_input('Would you like to play again? \'yes\'? ').lower() == 'yes':
            play_again = True
            game_over = False
        else:
            play_again = False
