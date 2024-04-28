# BLACKJACK-AI IU LUDDY CSCI-B 351 Spring 2024 Final Project

When dealing with artificial intelligence and gaming, the challenge that arises is not in understanding the game but rather in strategically navigating them to optimize outcomes. As a team, we dived into the dynamic project of creating an intelligent algorithm that would be proficient in Blackjack by employing advanced search algorithms.

## Description

Our project aims to develop an AI algorithm capable of comprehending the rules of Blackjack, executing strategic moves within the game, and progressively improving its gameplay through advanced search algorithms. Furthermore, we have implemented in parallel different algorithms in order to analyze them together and understand which ones perform better and why. 

### Project Structure
Our project is structured with 3 different files: Game.py, Player.py, Player_Test.py. 

#### Game.py
The Game file contains the code for a Game class that simulates a standard Blackjack game with 2 to 7 players and 1 to 4 decks. It simulates and creates a board and takes into account what the different choices of each players are.

#### Player.py
The Player file contains a list of Player classes we have created which are able to play a standard Blackjack game. It imports the Game class. There are currently 6 different player classes in the Player file:
* Dealer
* ManualPlayer
* RandomPlayer
* CardCountingPlayer
* NearestNeighborPlayer
* MinimaxPlayer

#### Player_Test.py
The Player_Test file is used to simulate a set number of games using different players and output their results for analysis. By default it simulates a 1000 games with 4 players (Dealer, RandomPlayer, MinimaxPlayer, and a NearestNeighborPlayer).

## Getting Started

### Dependencies

Our program doesn't require much to run and can run on any machine capable of running python 3. Here is a list of all the tools and libraries used:
* Python 3
* copy library (from python)
* random library (from python)
* matplotlib
* Any computer and OS capable of runing Python 3

### Executing program

* Using any code editor or computer terminal, run our main file (Player_Test.py) 
* The file will run and, by default, will simulate a 1000 Blackjack games
* The 1000 games involve a Dealer, RandomPlayer, MinimaxPlayer, and a NearestNeighborPlayer
* All of this is by default and can be customized, look at code snippet bellow (code from Player_Test.py)
```
# initialize players, game, and number of games
players = [Dealer(), RandomPlayer(), MinimaxPlayer(player_num=2), NearestNeighborPlayer()]
game = Game(len(players), decks=1)
num_games = 1000
```

## Authors

* Jalen Moya
* Jacob Mundy
* Thierry-Pascal Fleurant 

## Acknowledgments

Special thanks to:
* Professor Saúl A. Blanco
* Mentors Sanjana and Sal