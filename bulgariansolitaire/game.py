
class Game:
    '''Bulgarian Solitaire game class.

    --initializer args--
        1st arg: Positive integer that represents the number of cards used in the game.

    --class variables--
        numCards: Positive integer that represents the number of cards used in the game.
        gameHistory: List containing all the pileSets (lists) of the most recent games for each step until convergence.
    '''
    def __init__(self, numCards):
        self.numCards = numCards
        self.reset_history()

    def reset_history(self):
        self.gameHist = []

    def remove_empty_piles(self, pileSet):
        newSet = list(filter((0).__ne__, pileSet))
        return newSet

    def run(self, pileSet):
        ''' Run a Bulgarian Solitair game.
        
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

        while(newSet != self.gameHist[-1] and newSet not in self.gameHist):

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
