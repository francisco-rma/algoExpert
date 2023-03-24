import string

def generateDocument(document: string, source: string):

    def generateCharCount(term: string):
        charArray = list(term)
        charCount = {}
        for index, char in enumerate(charArray):
            if char in charCount.keys():
                charCount[char] += 1
            else:
                charCount[char] = 1

        return charCount

    if not document:
        return True

    isValid = False

    docCharCount = generateCharCount(document)
    sourceCharCount = generateCharCount(source)

    for char, count in docCharCount.items():
        if char in sourceCharCount.keys():
            sourceCount = sourceCharCount[char]
            if sourceCount < count or sourceCount is None:
                isValid = False
                return isValid
        else:
            isValid = False
            return isValid

        isValid = True

    return isValid
