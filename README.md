# War_game
The completed project is a popular card game called war. The game was made in Python with the help of object oriented programming.
# Suit class
The instances of this class shall have two instance attributes: description and symbol.
Description can be either: "clubs", "diamonds", "hearts", or "spades".
Symbol can be either: ♣, ♦, ♥, or ♠
# Card class
The instances of this class have two instance attributes: suit and value.
Suit is an instance of the Suit class.
The class has two methods: show and is_special.
The show method  displays the value, suit, and symbol of the suit of the card. If the card is special, the description is written (e.g. "Jack") instead of the value.
The is_special method  returns True if the value of the card is greater than or equal to 11 and False otherwise.
# Deck class
The instances of this class has one instance attribute: cards. This attribute is non-public and it shall contain a list of instances of the Card class (these are the cards that belong to the deck).
The deck has a property called size, which corresponds to the length of the list of cards in the deck.
The user of the Deck class is able to choose if the deck is initially empty or not when the deck instance is created.
The class has four methods: build, show, shuffle, draw, and add.
The build method builds the deck by creating 52 card instances with numbers from 2 to 14 (inclusive) for each one of the four possible suits.
The show method iterates over the list of card instances and call their show method to show the description of each card.
The shuffle method  shuffles the deck (the list of cards in the deck) by calling the shuffle function from the random module. 
The draw method returns and removes the last card in the list of cards in the deck.
The add method inserts a new card object to the beginning of the list of cards in the deck).
# Player class
The instances of this class have three instance attributes: name, deck, and is_computer. Name is a string. Deck isan instance of the Deck class.
is_computer is either True or False.
Name is a public attribute and deck and is_computer is non-public read-only attributes.
The class has four methods: has_empty_deck, draw_card, and add_card.
The has_empty_deck method returns True if the size of the player's deck is 0. Else, it returns False.
The draw_card  draws a card from the player's deck if the deck is not empty and return it.
The add_card method  adds a card to the bottom of the player's deck.
