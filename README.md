# BulgarianSolitaire

BulgarianSolitaire is a game simulator for the mathematical problem introduced by Martin Gardner in 1983.

Bulgarian Solitaire is played as follows: a fixed number of playing cards is divided into several piles. The quantity of
cards per pile is up to the player's choice. Then at each turn, one card is removed from each pile and are placed in a
separate pile. Piles of zero cards are ignored, and the piles of cards are sorted from lowest to highest number of cards.

The game ends once one of two conditions are met: (1) the pile configuration (# of piles in each pile) converges (repeats
after subsequent turns), or (2) the pile configuration reaches a cycle (repeats itself every ___ turns).

## Requirements

The package was tested for the following Python version:

* Python 3.5

## Installation

Download and unzip repository, or clone using the following command in a terminal in the directory you want to install:

`git clone https://github.com/mathieuboudreau/BulgarianSolitaire`

## Tests

To ensure the package is working as intended, in a terminal session go to the package folder and execute the following
command:

`python -m unittest`

## Usage

To run a game using a given starting pile set (e.g. [1, 8, 2, 9], where the numbers represents the number of cards in each
pile), run the following commands from a Python session:

```python
import bulgariansolitaire as bs

bsGame = bs.Game();

gameloSolution = bsGame.run([1, 8, 2, 9]);
```

The converged solution (either a single pile or a set of piles that loop) are returned by the run call (saved here in 
gameloSolution). The history of moves for the previously played game is stored in the `Game` object parameter `gameHist`.

To view the set of piles for the previously played game in a more human-friendly format than a list of lists, you can call
the following method:

```python
bsGame.print_history()
```

## About me

**Mathieu Boudreau** is a PhD Candidate at McGill University in the Department of Biomedical Engineering.
He holds a BSc in Physics from the Universite de Moncton ('09), and a MSc in Physics from the University 
of Western Ontario ('11).
