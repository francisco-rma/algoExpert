def firstNonRepeatingCharacter(string):

    usedChars = set()

    poolSet = []
    firstNRC = ''
    firstIndex = -1

    for index, value in enumerate(string):
        if index == 0:
            firstNRC = value
            firstIndex = index
            usedChars.add(value)
            continue

        if value not in usedChars:
            usedChars.add(value)
            poolSet.insert(0, (index, value))

        else:
            poolSet = [item for item in poolSet if item[1] != value]

        if value == firstNRC or firstNRC == '':

            if len(poolSet) > 0:
                firstIndex, firstNRC = poolSet.pop()

            else:
                firstIndex = -1
                firstNRC = ''
    return firstIndex
