def get_search_space(totalSet):

    def _addend_search(addendSet):
        ''' Generator that returns an addend set (set of numbers which add up to a given number)

            To return the complete set, the arg (addendSet) should be the longest addend, i.e. the
            set of ones of length equal to the total sum of the addends.

            i.e. To find all the sets of numbers which add up to 6, the initial argument should be
            [1, 1, 1, 1, 1, 1].

            --arg--
                addendSet: list of integers.
        '''
        yield addendSet # First call to generator should return the initial set from the generator arg.

        while len(addendSet) > 1:
            # An addend of length (len(addendSet)-1) can be created by summing the two last values of the a list of length
            # 2 or more
            addendSet = addendSet[:-2] + [addendSet[-2] + addendSet[-1]]

            yield addendSet

    longestAddend = [1] * totalSet; # Simplest case of set of ones which add up to totalSet.

    return list(_addend_search(longestAddend))
