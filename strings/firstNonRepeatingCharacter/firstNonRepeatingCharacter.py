
def firstNonRepeatingCharacter(string):
    poolSet = []
    first = ''
    idx = 0
    for index, value in enumerate(string):
        if index == 0:
            first = value
            idx = index
            poolSet.insert(0, value)

        elif value == first:
            poolSet.remove(value)

            if len(poolSet) > 0:
                first = poolSet.pop()
                idx = index
            else:
                first = ''
                idx = -1

        elif value in poolSet:
            poolSet.remove(value)

        else:
            poolSet.insert(0, value)

    return idx
