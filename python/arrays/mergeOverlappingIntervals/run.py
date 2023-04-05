from mergeOverlappingIntervals import mergeOverlappingIntervals as moi
from closeSolution import mergeOverlappingIntervals as cmoi
from newTry import mergeOverlappingIntervals as nmoi

array = [
    [43, 49],
    [9, 12],
    [12, 54],
    [45, 90],
    [91, 93]
]

longestPeak = nmoi(array)

print(longestPeak)
