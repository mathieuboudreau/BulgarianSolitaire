
class Game:
    '''Bulgarian Solitaire game class.

    --initializer args--
        (optional) 1st arg: Positive integer that represents the number of cards used in the game. 

    --class variables--
        numCards: Positive integer that represents the number of cards used in the game.
        gameHistory: List containing all the pileSets (lists) of the most recent games for each step until convergence.

    --methods--
        run(pileSet): Executes a Bultarian Solitaire game with the starting piles of cards described by the argument (list of 
                      integers). Zero piles are ignored. The history of the card piles following each game loop are saved in 
                      the class variable "gameHistory" as a list of lists, and is also returned by the method call. Each
                      call of run will reset the previous gameHistory variable prior to saving the current game.

                      Example: run([1 9 10]) will run a Bulgarian Solitaire games using 20 cards, using three piles (1, 9,
                      and 10 card tall).
    
        print_history(): Print the previous game history in a human readable format.

    '''
    def __init__(self, *args):
        if args:
            self.numCards = args[0]
        self.reset_history()

    def reset_history(self):
        self.gameHist = []

    def print_history(self):
        for pile in self.gameHist:
            print(pile)

    def remove_empty_piles(self, pileSet):
        return list(filter((0).__ne__, pileSet))

    def run(self, pileSet):
        ''' Run a Bulgarian Solitaire game.
        
        Each game step until the solution is saved in the instance variable "gameHist".
        Returns self.gameHist
        
        --args--
            pileSet: list of integers that represents the piles of cards.
        '''
        self.numCards = sum(pileSet)
 
        pileSet = self.remove_empty_piles(pileSet)
        pileSet = sorted(pileSet)

        self.reset_history()
        self.gameHist.append(pileSet)

        newSet = []

        while(newSet not in self.gameHist):

            if newSet: # Required so that the first set isn't saved twice
                self.gameHist.append(newSet)

            # Remove 1 card from each pile, and form a new pile
            newPile = len(pileSet)
            newSet = [x - 1 for x in pileSet]
            newSet.append(newPile)
            newSet = self.remove_empty_piles(newSet)

            # Sort the piles
            newSet = sorted(newSet)

            # Save as the pileSet, if needed for next iteration
            pileSet = newSet

        return self.gameHist
