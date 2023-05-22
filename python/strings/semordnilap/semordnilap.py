def semordnilap(words):
    pairs = set()

    def isSemordnilap(string1, string2):
        isSemordnilap = False

        if len(string1) != len(string2):
            return isSemordnilap

        size = len(string1)

        for index, value in enumerate(string1):
            if value != string2[size - index - 1]:
                isSemordnilap = False
                return isSemordnilap

        isSemordnilap = True

        return isSemordnilap

    for index, value in enumerate(words):
        for textIndex, testValue in enumerate(words[index + 1:]):
            if isSemordnilap(value, testValue):
                pairs.add((value, testValue))

    return pairs
