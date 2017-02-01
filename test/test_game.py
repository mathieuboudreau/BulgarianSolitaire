import unittest
import bulgariansolitaire as bs

class GameTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    # Initializer
    def test_that_first_class_arg_is_stored_to_correct_variable(self):
        gameSession = bs.Game(10)

        self.assertEqual(gameSession.numCards, 10)

    # Methods
    def test_that_remove_empty_piles_removes_zeros_from_list(self):
        self.assertEqual(bs.Game.remove_empty_piles([1, 0, 3, 0, 0, 2]), [1, 3, 2])
        
