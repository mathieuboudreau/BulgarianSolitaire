import unittest
import bulgariansolitaire as bs

class GetSeachSpaceTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    # Return Types
    def test_that_get_search_space_returns_list(self):
        assert isinstance(bs.get_search_space(1), list)