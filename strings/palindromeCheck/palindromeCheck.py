def isPalindrome(string):
    isPalindrome = False

    size = len(string)

    for index, value in enumerate(string):
        if value != string[size - index - 1]:
            isPalindrome = False
            return isPalindrome

    isPalindrome = True

    return isPalindrome
