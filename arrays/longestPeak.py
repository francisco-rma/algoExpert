def longestPeak(array):
    peak = []
    peakCount = 0
    maxLength = 0

    peakStart = True
    # peakEnd = False

    increasing = False
    increased = False

    for index, value in enumerate(array):
        if index < len(array) - 1:
            if value == array[index + 1]:
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peakStart = True
                peak = []
                continue

            if array[index + 1] > value:
                increasing = True

            else:
                increasing = False

            if index != 0:
                if array[index - 1] < value:
                    increased = True

                else:
                    increased = False

            if increasing and peakStart:
                peak.append(value)
                continue

            elif increasing and not peakStart:
                peak.append(value)
                peakStart = True
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peak = [value]
                continue

            elif not increasing and peakStart:
                if increased:
                    peakStart = False
                    peakCount += 1
                    peak.append(value)
                    continue

                else:
                    peakStart = True
                    if len(peak) > maxLength:
                        maxLength = len(peak)
                    peak = []
                    continue

            elif not increasing and not peakStart:
                peakStart = False
                peak.append(value)
                continue

        else:

            if value == array[index - 1]:
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peakStart = True
                peak = []
                continue

            print(f'valor anterior: ${array[index - 1]}')

            if array[index - 1] < value:
                increased = True

            else:
                increased = False

            if increased and peakStart:
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peak = []
                continue

            elif increased and not peakStart:
                peakStart = True
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peak = []
                continue

            elif not increased and peakStart:
                peakStart = True
                if len(peak) > maxLength:
                    maxLength = len(peak)
                peak = []
                continue

            elif not increased and not peakStart:
                peakStart = False
                peak.append(value)
                if len(peak) > maxLength:
                    maxLength = len(peak)
                continue

    if peakCount == 0 or maxLength < 3:
        maxLength = 0

    return maxLength
