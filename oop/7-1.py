class Card:
    def __init__(self, number, mark):
        self.number = number
        self.mark = mark


class Deck:
    MARKS = ["spade", "diamond", "club", "heart"]

    def __init__(self):
        self.cards = []

        # 本当はジョーカーがいるけど、ブラックジャックでは使わないので考えない
        for mark in self.MARKS:
            self.cards.extend([Card(number, mark) for number in range(1, 14)])

    def shuffle(self, times):
        for _ in times:
            for card_from_first_half, card_from_second_half in zip(self.cards[:26], self.cards[26:]):

    def hand_out(self):
        return self.cards.pop(-1)


class Player:
    def __init__(self, is_dealer, on_deal=True):
        self.cards = []
        self.is_dealer = is_dealer
        self.on_deal = on_deal

    def draw(self, card):
        self.cards.append(card)

    def score(self):
        return sum([card.number for card in self.cards])


def init_game(deck, dealer, players):
    deck.shuffle()
    dealer.draw()


def play_blackjack():
    deck = Deck()
    dealer = Player(is_dealer=True)
    players = [Player(is_dealer=False) for _ in range(3)]

    while True:
        decision = input("ヒット or スタンド")
        # プレイヤーがヒットかスタンドを選ぶ
        # プレイヤーの持ち札が21を超えるか、スタンドでカードを引くのをやめるかしたら、player.on_dealをfalseにする
        # 全プレイヤーのon_dealがfalseになったらwhileを抜ける
        break

    while dealer.score() < 17:
        # ディーラーは17を超えるまで引き続ける
        dealer.draw(deck.hand_out())

    # 一番21に近いやつが勝ち


if __name__ == "__main__":
    deal_blackjack()
