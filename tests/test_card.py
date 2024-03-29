import unittest
from poker.card import Card


class CardTes(unittest.TestCase):
    def test_card_has_rank(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_card_has_suit(self):
        card = Card(rank="2", suit="Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_card_has_strings(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_technical_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5','Diamonds')")

    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(Card.SUITS, ("Hearts", "Clubs", "Diamonds", "Spades"))

    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(Card.RANKS, ("2", "3", "4", "5",
                                      "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"))

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Spades")

    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank="2", suit="Spade")
