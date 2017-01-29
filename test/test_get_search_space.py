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

    # Return known cases
    def test_that_get_search_space_returns_the_longest_set_case(self):
        self.assertTrue([1,1,1,1] in bs.get_search_space(4))

    def test_that_get_search_space_returns_the_single_value_case(self):
        self.assertTrue([5] in bs.get_search_space(5))

    def test_that_get_search_space_returns_the_recursive_cases(self):
        self.assertTrue([1, 2, 2] in bs.get_search_space(5))

    # Ensure no duplicates in set
    def test_that_get_search_space_returns_no_duplicates(self):

        searchList = bs.get_search_space(5)
        uniquesList = []
        for elem in searchList:
            elem = sorted(elem) # Sets are equal regardless of order for our purpose
            if elem not in uniquesList:
                uniquesList.append(elem)

        self.assertTrue(len(uniquesList)==len(searchList))
