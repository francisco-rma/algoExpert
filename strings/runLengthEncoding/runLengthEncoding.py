def encoder(string):
    encodedString = ""

    i = 0

    charArray = list(string)

    runningChar = charArray[0]
    runningCharCount = 0

    while i < len(charArray):
        char = charArray[i]

        if char != runningChar or runningCharCount == 9:
            encodedString = encodedString + f"{runningCharCount}{runningChar}"
            runningChar = char
            runningCharCount = 1
            i += 1
            continue

        else:
            runningCharCount += 1
            i += 1
            continue
    
    encodedString = encodedString + f"{runningCharCount}{runningChar}"
    
    return encodedString
