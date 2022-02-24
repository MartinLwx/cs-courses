## Magic: the Lambda-ing

In the next part of this lab, we will be implementing a card game! This game is inspired by the similarly named[Magic: The Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering).

Once you've implemented the game, you can start it by typing:

```bash
python3 cardgame.py
```

While playing the game, you can exit it and return to the command line with `Ctrl-C` or `Ctrl-D`.

This game uses several different files.

-   Code for all the questions in this lab can be found in `classes.py`.
-   Some utility for the game can be found in `cardgame.py`, but you won't need to open or read this file. This file doesn't actually mutate any instances directly - instead, it calls methods of the different classes, maintaining a strict abstraction barrier.
-   If you want to modify your game later to add your own custom cards and decks, you can look in `cards.py` to see all the standard cards and the default deck; here, you can add more cards and change what decks you and your opponent use. If you're familiar with the original game, you may notice the cards were not created with balance in mind, so feel free to modify the stats and add or remove cards as desired.

### Rules of the Game

This game is a little involved, though not nearly as much as its namesake. Here's how it goes:

There are two players. Each player has a hand of cards and a deck, and at the start of each round, each player draws a random card from their deck. If a player's deck is empty when they try to draw, they will automatically lose the game. Cards have a name, an attack value, and a defense value. Each round, each player chooses one card to play from their own hands. The card with the higher *power* wins the round. Each played card's power value is calculated as follows:

```
(player card's attack) - (opponent card's defense) / 2
```

For example, let's say Player 1 plays a card with 2000 attack and 1000 defense and Player 2 plays a card with 1500 attack and 3000 defense. Their cards' powers are calculated as:

```
P1: 2000 - 3000/2 = 2000 - 1500 = 500
P2: 1500 - 1000/2 = 1500 - 500 = 1000
```

So Player 2 would win this round.

The first player to win 8 rounds wins the match!

However, there are a few effects we can add (in the optional questions section) to make this game a more interesting. A card can be of type AI, Tutor, TA, or Instructor, and each type has a different *effect* when they are played. All effects are applied before power is calculated during that round:

-   An AI card will reduce the opponent card's attack by the opponent card's defense, and then double the opponent card's defense.
-   A Tutor card will cause the opponent to discard and re-draw the first 3 cards in their hand.
-   A TA card will swap the opponent card's attack and defense.
-   An Instructor card will add the opponent card's attack and defense to all cards in their deck and then remove all cards in the opponent's deck that share its attack *or* defense!

Feel free to refer back to these series of rules later on, and let's start making the game!