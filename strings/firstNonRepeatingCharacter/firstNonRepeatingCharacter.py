
# def firstNonRepeatingCharacter(string):
#     poolSet = {}
#     first = ''

#     for index, value in enumerate(string):
#         if index == 0:
#             first = value
#             poolSet[value] = index
#         elif value == first:
#             poolSet.pop(value)

#         elif value in poolSet:
#             poolSet.pop(value)

#         else:
#             poolSet[value] = index

#     return poolSet[first]


def firstNonRepeatingCharacter(string):
    poolSet = {}
    first = {}
    for index, value in enumerate(string):
        if index == 0:
            first[value] = index
            poolSet[value] = index
        elif value == first:
            poolSet.pop(value)

            if len(poolSet) > 0:
                first = poolSet.popitem()

        elif value in poolSet:
            poolSet.pop(value)

        else:
            poolSet[value] = index

    index, value = first.pop()
    return index
