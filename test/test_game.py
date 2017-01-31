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
